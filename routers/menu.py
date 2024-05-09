from fastapi import APIRouter,Depends,HTTPException,Body,status
from sqlalchemy.orm import Session
import schemas,crud
from dependencies import get_db

router=APIRouter(
    prefix="/menu",
    tags=["Pizza menu"],
)

@router.get("",response_model=schemas.getPizzaResponse,status_code=status.HTTP_200_OK)
async def get_Pizza_menu(db:Session=Depends(get_db)):
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