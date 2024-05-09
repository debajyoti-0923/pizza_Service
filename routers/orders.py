from fastapi import APIRouter,Depends,HTTPException,Body,status
from sqlalchemy.orm import Session
import schemas,crud
from dependencies import get_db

router=APIRouter(
    prefix="/order",
    tags=["Order"],
)

def generateCart(resModel):
    cartItems=[]
    orderPrice=0
    priorityPrice=0
    for item in resModel.cart:
        totalPrice=(item.pizza.unitPrice)*(item.quantity)
        orderPrice+=totalPrice
        priorityPrice+=item.pizza.priorityPrice
        k=schemas.orderCartItem(
            pizzaId=item.pizzaId,
            name=item.pizza.name,
            quantity=item.quantity,
            unitPrice=item.pizza.unitPrice,
            totalPrice=totalPrice,
            addIngredients=[addItem.ingredients.name for addItem in item.addIngs],
            removeIngredients=[remItem.ingredients.name for remItem in item.removeIngs],
            additionalNote="" if item.addNotes is None else item.addNotes
        )
        cartItems.append(k)
    return orderPrice,priorityPrice,cartItems

@router.post("",response_model=schemas.outOrderResponse,status_code=status.HTTP_200_OK)
async def addOrder(odr:schemas.addOrder,db:Session=Depends(get_db)):
    res=crud.add_order(db,odr)
    if res is None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail={"message":"some error while fetching"})
    
    resModel=crud.get_order(db,res)
    if resModel is None or resModel==False:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail={"message":"some error while fetching"})
    
    orderPrice,priorityPrice,cartItems=generateCart(resModel)
    outResData=schemas.orderCartResponse(
        status=resModel.status,
        id=resModel.orderId,
        createdAt=resModel.createdAt,
        estimatedDelivery=resModel.estimatedDelivery,
        orderPrice=orderPrice,
        priorityPrice=priorityPrice if resModel.priority else 0,
        customer=resModel.customer,
        priority=resModel.priority,
        cart=cartItems,
        phone=resModel.phone,
        address=resModel.address,
        position=""
    )
    return schemas.outOrderResponse(status="success",data=outResData)

    
@router.get("/{odrId}",response_model=schemas.outOrderResponse,status_code=status.HTTP_200_OK)
async def getByID(odrId:str,db:Session=Depends(get_db)):
    if odrId is None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail={"message":"some error while fetching"})
    
    resModel=crud.get_order(db,odrId)
    if resModel is None or resModel==False:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail={"message":"some error while fetching"})
    
    orderPrice,priorityPrice,cartItems=generateCart(resModel)
    outResData=schemas.orderResponse(
        status=resModel.status,
        id=resModel.orderId,
        createdAt=resModel.createdAt,
        estimatedDelivery=resModel.estimatedDelivery,
        orderPrice=orderPrice,
        priorityPrice=priorityPrice if resModel.priority else 0,
        customer=resModel.customer,
        priority=resModel.priority,
        cart=cartItems,
    )
    return schemas.outOrderResponse(status="success",data=outResData)

    
@router.patch("/{odrId}",status_code=status.HTTP_204_NO_CONTENT)
async def makePriority(odrId:str,details:schemas.orderPatch,db:Session=Depends(get_db)):
    if odrId is None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail={"message":"some error while fetching"})
    crud.makePriorityOrder(db,odrId)