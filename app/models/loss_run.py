from beanie import Document
from pydantic import Field
from datetime import date

class LossRun(Document):
    driver_id: str = Field(...)
    loss_date: date = Field(...)
    amount: float = Field(...)

    class Settings:
        name = "lossruns"