from fastapi import APIRouter,Depends,HTTPException,Body,status
from sqlalchemy.orm import Session
import schemas,crud
from dependencies import get_db

router=APIRouter(
    prefix="/ingredients",
    tags=["Ingredients"]  
)

@router.get("/get",response_model=schemas.getIngredientsResponse,status_code=status.HTTP_200_OK)
async def getIngredietns(db:Session=Depends(get_db)):
    resModels=crud.get_ingredients(db)
    if resModels is None or resModels==[]:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail={"message":"some error while fetching"})
    data=[]
    for i in resModels:
        data.append(schemas.getIngredients(id=i.id,name=i.name))
    return schemas.getIngredientsResponse(status="success",data=data)


@router.post("/add",response_model=schemas.response,status_code=status.HTTP_200_OK)
async def addIngredient(ing:schemas.addIngredient,db:Session=Depends(get_db)):
    res=crud.add_ingredients(db,ing)
    if res:
        return schemas.response(status="success")
    else:
        return schemas.response(status="fail")
    

@router.patch("/update")
async def update_Ingredients_Details(details:schemas.ingredientPatch,db:Session=Depends(get_db)):
    res=crud.patchIngredients(db,details)
    print(res)
    if res:
        return schemas.response(status="ok")
    else:
        return schemas.response(status="fail")
