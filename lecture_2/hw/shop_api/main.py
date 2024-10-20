from fastapi import FastAPI
from lecture_2.hw.shop_api.routers.cartRouter import cartRouter
from lecture_2.hw.shop_api.routers.itemRouter import itemRouter
from prometheus_fastapi_instrumentator import Instrumentator

app = FastAPI(title="Shop API")
Instrumentator().instrument(app).expose(app)

app.include_router(cartRouter)
app.include_router(itemRouter)