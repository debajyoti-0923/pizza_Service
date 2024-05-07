from sqlalchemy import Boolean,Integer,String,Column,ForeignKey,DATETIME
from database import Base
from sqlalchemy.orm import Mapped,mapped_column,relationship
from datetime import datetime
class PizzaInv(Base):
    __tablename__='inventory'

    id:Mapped[int]=mapped_column(Integer,primary_key=True,index=True)
    name:Mapped[str]=mapped_column(String(50),nullable=False)
    unitPrice:Mapped[int]=mapped_column(Integer,nullable=False)
    priorityPrice:Mapped[int]=mapped_column(Integer,nullable=False)
    imageUrl:Mapped[str]=mapped_column(String(150),nullable=False)
    soldOut:Mapped[bool]=mapped_column(Boolean,nullable= False,default=False)
    preparingTime:Mapped[int]=mapped_column(Integer,nullable= False)
    pizzaIngredients:Mapped[list["PizzaIngredients"]]=relationship(back_populates="pizza")
    cart:Mapped[list["Cart"]]=relationship(back_populates="pizza")

class Ingredients(Base):
    __tablename__='ingredients'

    id:Mapped[int]=mapped_column(Integer,primary_key=True,index=True)
    name:Mapped[str]=mapped_column(String(20),nullable=False)
    pizzaIngredients:Mapped[list["PizzaIngredients"]]=relationship(back_populates="ingredients")
    addIngs:Mapped[list["addIngredients"]]=relationship(back_populates="ingredients")
    removeIngs:Mapped[list["removeIngredients"]]=relationship(back_populates="ingredients")

class PizzaIngredients(Base):
    __tablename__='pizzaIngredients'

    id:Mapped[int]=mapped_column(Integer,primary_key=True,index=True)
    pizzaId:Mapped[int]=mapped_column(ForeignKey("inventory.id"))
    ingredientId:Mapped[int]=mapped_column(ForeignKey("ingredients.id"))
    pizza:Mapped["PizzaInv"]=relationship(back_populates="pizzaIngredients")
    ingredients:Mapped["Ingredients"]=relationship(back_populates="pizzaIngredients")

class Orders(Base):
    __tablename__='orders'

    id:Mapped[int]=mapped_column(Integer,primary_key=True,index=True)
    orderId:Mapped[str]=mapped_column(String(6),unique=True,nullable=False)
    customer:Mapped[str]=mapped_column(String(30),nullable= False)
    phone:Mapped[int]=mapped_column(Integer)
    address:Mapped[str]=mapped_column(String(200))
    status:Mapped[str]=mapped_column(String(20))
    priority:Mapped[bool]=mapped_column(Boolean,default=False)
    createdAt:Mapped[datetime]=mapped_column(DATETIME,nullable=False)
    estimatedDelivery:Mapped[datetime]=mapped_column(DATETIME,nullable=False)
    cart:Mapped[list["Cart"]]=relationship(back_populates="orders")

class Cart(Base):
    __tablename__='cart'

    id:Mapped[int]=mapped_column(Integer,primary_key=True,index=True)
    orderId:Mapped[int]=mapped_column(ForeignKey("orders.id"))
    pizzaId:Mapped[int]=mapped_column(ForeignKey("inventory.id"))
    quantity:Mapped[int]=mapped_column(Integer,nullable=False)
    addNotes:Mapped[str]=mapped_column(String(100),nullable=True)
    orders:Mapped["Orders"]=relationship(back_populates="cart")
    pizza:Mapped["PizzaInv"]=relationship(back_populates="cart")
    addIngs:Mapped[list["addIngredients"]]=relationship(back_populates="cart")
    removeIngs:Mapped[list["removeIngredients"]]=relationship(back_populates="cart")

class addIngredients(Base):
    __tablename__='addIngredients'

    id:Mapped[int]=mapped_column(Integer,primary_key=True,index=True)
    cartId:Mapped[int]=mapped_column(ForeignKey("cart.id"))
    ingredientId:Mapped[int]=mapped_column(ForeignKey("ingredients.id"))
    cart:Mapped["Cart"]=relationship(back_populates="addIngs")
    ingredients:Mapped["Ingredients"]=relationship(back_populates="addIngs")


class removeIngredients(Base):
    __tablename__='removeIngredients'

    id:Mapped[int]=mapped_column(Integer,primary_key=True,index=True)
    cartId:Mapped[int]=mapped_column(ForeignKey("cart.id"))
    ingredientId:Mapped[int]=mapped_column(ForeignKey("ingredients.id"))
    cart:Mapped["Cart"]=relationship(back_populates="removeIngs")
    ingredients:Mapped["Ingredients"]=relationship(back_populates="removeIngs")

