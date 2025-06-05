from app.models.loss_run import LossRun

class LossRunRepository:

    @staticmethod
    async def create(data: dict) -> LossRun:
        loss_run = LossRun(**data)
        return await loss_run.insert()

    @staticmethod
    async def get_all():
        return await LossRun.find_all().to_list()