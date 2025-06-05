from app.repositories.loss_run_repository import LossRunRepository
from app.schemas.loss_run_schema import LossRunIn

class LossRunService:

    @staticmethod
    async def create_loss_run(loss_run_in: LossRunIn):
        return await LossRunRepository.create(loss_run_in.dict())

    @staticmethod
    async def get_all_loss_runs():
        return await LossRunRepository.get_all()