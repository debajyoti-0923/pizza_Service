from pydantic import BaseModel,Field,EmailStr
from typing import Optional,Literal,Union
from datetime import datetime

class response(BaseModel):
    status:str=Field(...)

class Pizza(BaseModel):
    name:str=Field(...,description="name of the pizza")
    unitPrice:int=Field(...,description="price of pizza")
    priorityPrice:int=Field(...,description="priority order cost")
    imageUrl:str=Field(...,description="pizza image")
    soldOut:bool=Field(...,description="in stock or not")
    preparingTime:int=Field(...,description="time to prepare the order")
    ingredients:list[str]=Field(...,description="name of ingredients")

class addPizza(Pizza):
    pass
class getPizza(Pizza):
    id:int=Field(...,description="id of pizza")

class getPizzaResponse(response):
    data:list[getPizza]=Field(...)

#-------------------------------------------------------------

class Ingredient(BaseModel):
    name:str=Field(...,description="name of ingredient")

class addIngredient(Ingredient):
    pass

class getIngredients(Ingredient):
    id:int=Field(...,description="id of ingredient")

class getIngredientsResponse(response):
    data:list[getIngredients]=Field(...)

#-------------------------------------------------------

class orderCartItem(BaseModel):
    pizzaId:int=Field(...,description="id of the pizza")
    name:str=Field(...,description="name of pizza")
    quantity:int=Field(...,description="quantity of item")
    unitPrice:int=Field(...,description="price of the item")
    totalPrice:int=Field(...,description="total price of item")
    addIngredients:Optional[list[str]]=Field(None,description="extra ingredients to add")
    removeIngredients:Optional[list[str]]=Field(None,description="ingredients to remove")
    additionalNote:Optional[str]=Field(None,description="any extra notes with order")

class order(BaseModel):
    customer:str=Field(...,description="name of customer")
    priority:bool=Field(...,description="order is priority or not")
    cart:list[orderCartItem]=Field(...,description="items in cart")

class addOrder(order):
    phone:int=Field(...,description="phone number of customer")
    address:str=Field(...,description="delivery address")
    position:str=Field(...)

class orderResponse(order):
    status:Literal["preparing","delivered"]=Field(...,description="status of order")
    id:str=Field(...,description="order id")
    createdAt:datetime=Field(...,description="datetime when order placed")
    estimatedDelivery:datetime=Field(...,description="estimated delivery time")
    orderPrice:int=Field(...,description="total order cost")
    priorityPrice:int=Field(...,description="priority price of order")

class orderCartResponse(orderResponse,addOrder):
    pass

class outOrderResponse(response):
    data:Union[orderCartResponse,orderResponse]

class orderPatch(BaseModel):
    priority:bool