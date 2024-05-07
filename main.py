from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import models
from database import engine,SessionLocal
from sqlalchemy.orm import Session
from dependencies import get_db
import crud
import asyncio
from contextlib import asynccontextmanager
import httpx

class BackgroundRunner:
    async def run_main(self):
        while True:
            db:Session=next(get_db())
            print("check updates func")
            crud.update_status(db)
            await asyncio.sleep(60)

class SelfPinger:
    def __init__(self):
        self.task = None

    async def self_ping(self, url: str):
        async with httpx.AsyncClient() as client:
            while True:
                try:
                    response = await client.get(url)
                    print(f"Self-ping response status code: {response.status_code}")
                except:
                    pass
                await asyncio.sleep(600)  

    def start_ping(self, url: str):
        self.task = asyncio.create_task(self.self_ping(url))

    async def stop_ping(self):
        if self.task:
            self.task.cancel()
            try:
                await self.task
            except asyncio.CancelledError:
                pass

self_pinger = SelfPinger()

runner = BackgroundRunner()

@asynccontextmanager
async def lifespan(app: FastAPI):
    print("starting background task")
    asyncio.create_task(runner.run_main())
    yield
    await self_pinger.stop_ping()


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

@app.get("/keepalive/{link}")
async def keepAlive(link:str):
    url=f"https://{link}.onrender.com/"
    if self_pinger.task is not None:
        await self_pinger.stop_ping()
    self_pinger.start_ping(url)
    return {"message": f"Self-ping initiated at {url}"}