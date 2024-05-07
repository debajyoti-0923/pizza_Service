from fastapi import APIRouter,Depends,HTTPException,Body,status
from sqlalchemy.orm import Session
import schemas,crud
from dependencies import get_db

router=APIRouter(
    prefix="/pizza",
    tags=["pizza"],
)


@router.post("/add",response_model=schemas.response,status_code=status.HTTP_200_OK)
async def addPizza(piz:schemas.addPizza,db:Session=Depends(get_db)):
    res=crud.add_pizza(db,piz)
    if res:
        return schemas.response(status="success")
    else:
        return schemas.response(status="fail")
    
@router.get("/get",response_model=schemas.getPizzaResponse,status_code=status.HTTP_200_OK)
async def getPizza(db:Session=Depends(get_db)):
    resModels=crud.get_pizzas(db)
    if resModels is None or resModels==[]:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail={"message":"some error while fetching"})
    
    data=[]
    for i in resModels:
        ingredientsArr=[]
        for ings in i.pizzaIngredients:
            ingredientsArr.append(ings.ingredients.name)
        data.append(schemas.getPizza(
            id=i.id,
            name=i.name,
            unitPrice=i.unitPrice,
            priorityPrice=i.priorityPrice,
            imageUrl=i.imageUrl,
            soldOut=i.soldOut,
            preparingTime=i.preparingTime,
            ingredients=ingredientsArr
        ))

    return schemas.getPizzaResponse(status="success",data=data)