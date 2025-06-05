from fastapi import FastAPI
from app.db.init import init_db
from app.api.driver_routes import router as driver_router
from app.api.loss_run_routes import router as loss_run_router

app = FastAPI()
app.include_router(driver_router)
app.include_router(loss_run_router)

@app.on_event("startup")
async def on_startup():
    await init_db()