from app.repositories.driver_repository import DriverRepository
from app.schemas.driver_schema import DriverIn

class DriverService:

    @staticmethod
    async def create_driver(driver_in: DriverIn):
        return await DriverRepository.create(driver_in.dict())

    @staticmethod
    async def get_all_drivers():
        return await DriverRepository.get_all()