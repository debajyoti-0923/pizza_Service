from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import models
from database import engine,SessionLocal
from sqlalchemy.orm import Session
from dependencies import get_db
import crud
import asyncio
from contextlib import asynccontextmanager
import requests

class keepAliveRender:
    def __init__(self) -> None:
        self.link=None
    def createLink(self,link):
        return f"https://{link}.onrender.com"
    async def run_main(self):
        while True:
            if self.link is None:
                await asyncio.sleep(5)
                continue
            response = requests.get(self.link)
            await asyncio.sleep(840)

class BackgroundRunner:
    async def run_main(self):
        while True:
            db:Session=next(get_db())
            crud.update_status(db)
            await asyncio.sleep(60)
            

runner = BackgroundRunner()
keepAliveRunner=keepAliveRender()

@asynccontextmanager
async def lifespan(app: FastAPI):
    print("starting background task")
    asyncio.create_task(runner.run_main())
    asyncio.create_task(keepAliveRunner.run_main())
    yield

app=FastAPI(lifespan=lifespan)
models.Base.metadata.create_all(bind=engine)
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


from routers import ingredients,pizza,orders,menu
app.include_router(ingredients.router)
app.include_router(pizza.router)
app.include_router(orders.router)
app.include_router(menu.router)

@app.get("/")
async def getRoot():
    return {"message":"Hello from Debu's Pizza Service"}

@app.post("/keepalive/{link}")
async def keepAlive(link:str):
    keepAliveRunner.link=keepAliveRunner.createLink(link)