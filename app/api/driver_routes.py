from fastapi import APIRouter
from app.schemas.driver_schema import DriverIn, DriverOut
from app.services.driver_service import DriverService

router = APIRouter(prefix="/drivers", tags=["Drivers"])

@router.post("/", response_model=DriverOut)
async def create_driver(driver: DriverIn):
    return await DriverService.create_driver(driver)

@router.get("/", response_model=list[DriverOut])
async def get_all_drivers():
    return await DriverService.get_all_drivers()