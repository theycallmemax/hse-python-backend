from fastapi import FastAPI
from lecture_2.hw.shop_api.routers.cartRouter import cartRouter
from lecture_2.hw.shop_api.routers.itemRouter import itemRouter

app = FastAPI(title="Shop API")

app.include_router(cartRouter)
app.include_router(itemRouter)