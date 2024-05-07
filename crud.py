from sqlalchemy.orm import Session
import models,schemas,dependencies,database

#----------------------------------------------------------------
def get_pizzas(db:Session):
    res=db.query(models.PizzaInv).all()
    return res

def get_ingredients(db:Session):
    res=db.query(models.Ingredients).all()
    return res

def add_ingredients(db:Session,details:schemas.addIngredient):
    try:
        ing=models.Ingredients(**details.model_dump())
        db.add(ing)
        db.commit()
        return True
    except:
        return False
    
def add_pizza(db:Session,details:schemas.addPizza):
    try:
        row=models.PizzaInv(
            name=details.name,
            unitPrice=details.unitPrice,
            priorityPrice=details.priorityPrice,
            imageUrl=details.imageUrl,
            preparingTime=details.preparingTime,
            soldOut=details.soldOut
        )
        db.add(row)
        db.commit()
        
        for i in details.ingredients:
            ingredient=db.query(models.Ingredients).filter(models.Ingredients.name==i).first()
            r=models.PizzaIngredients(pizzaId=row.id,ingredientId=ingredient.id)
            db.add(r)
        db.commit()
        return True
    except:
        return False
    
def add_order(db:Session,details:schemas.addOrder):
    try:
        orderId=dependencies.get_order_id()

        timeRqd=0
        for cartItem in details.cart:
            p=db.query(models.PizzaInv).filter(models.PizzaInv.id==cartItem.pizzaId).first()
            timeRqd+=p.preparingTime

        if details.priority:
            timeRqd-=10

        row=models.Orders(
            orderId=orderId,
            customer=details.customer,
            phone=details.phone,
            address=details.address,
            status="preparing",
            priority=details.priority,
            createdAt=dependencies.get_current_time(),
            estimatedDelivery=dependencies.get_estimated_time(timeRqd)
        )
        db.add(row)
        db.commit()

        for cartItem in details.cart:
            cartModel=models.Cart(
                orderId=row.id,
                pizzaId=cartItem.pizzaId,
                quantity=cartItem.quantity,
                addNotes=cartItem.additionalNote
            )
            db.add(cartModel)
            db.commit()

            if cartItem.addIngredients is not None:
                for cartAddIng in cartItem.addIngredients:
                    res=db.query(models.Ingredients).filter(models.Ingredients.name==cartAddIng).first()
                    addIngModel=models.addIngredients(
                        cartId=cartModel.id,
                        ingredientId=res.id
                    )
                    db.add(addIngModel)
                    db.commit()
                    
            if cartItem.removeIngredients is not None:
                for cartRemIng in cartItem.removeIngredients:
                    res=db.query(models.Ingredients).filter(models.Ingredients.name==cartRemIng).first()
                    RemIngModel=models.removeIngredients(
                        cartId=cartModel.id,
                        ingredientId=res.id
                    )
                    db.add(RemIngModel)
                    db.commit()
        
        return orderId
    except:
        return False

def get_order(db:Session,orderId:str):
    res=db.query(models.Orders).filter(models.Orders.orderId==orderId).first()
    if res is not None:
        return res
    else:
        return False



def makePriorityOrder(db:Session,orderId:str):
    res=db.query(models.Orders).filter(models.Orders.orderId==orderId).first()
    if res is None or res.priority:
        return
    db.query(models.Orders).filter(models.Orders.orderId==orderId).update(
        {
            'priority':True,
            'estimatedDelivery':dependencies.get_estimated_time(-10,res.estimatedDelivery)
        },
        synchronize_session=False
    )
    db.commit()

def update_status(db:Session):
    print("checking deliviery status")
    res=db.query(models.Orders).filter(models.Orders.status=='preparing').all()
    for i in res:
        if dependencies.get_time_compare(i.estimatedDelivery):
            db.query(models.Orders).filter(models.Orders.id==i.id).update({'status':'delivered'},synchronize_session=False)
    db.commit()