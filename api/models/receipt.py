from sqlalchemy import Column, Integer, String, Numeric, DateTime, func
from sqlalchemy.ext.declarative import declarative_base
from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional

from database import Base


# SQLAlchemy модель для таблицы receipts
class ReceiptDB(Base):
    __tablename__ = "receipts"

    id = Column(Integer, primary_key=True, index=True)
    deleted_with_writeoff = Column(String(20), nullable=False)
    department = Column(String(100), nullable=False, index=True)
    dish_amount_int = Column(Numeric(15, 2), nullable=False)
    dish_code = Column(String(20), nullable=False)
    dish_discount_sum_int = Column(Numeric(15, 2), nullable=False)
    dish_measure_unit = Column(String(10), nullable=False)
    dish_name = Column(String(200), nullable=False)
    dish_sum_int = Column(Numeric(15, 2), nullable=False)
    order_num = Column(Integer, nullable=False, index=True)
    pay_types = Column(String(50), nullable=False, index=True)
    precheque_time = Column(DateTime, nullable=False, index=True)
    created_at = Column(DateTime, nullable=False, server_default=func.now())


# Pydantic модели для API

class ReceiptBase(BaseModel):
    """Базовая модель для чека"""
    deleted_with_writeoff: str
    department: str
    dish_amount_int: float
    dish_code: str
    dish_discount_sum_int: float
    dish_measure_unit: str
    dish_name: str
    dish_sum_int: float
    order_num: int
    pay_types: str
    precheque_time: datetime


class ReceiptCreate(ReceiptBase):
    """Модель для создания чека"""
    pass


class Receipt(ReceiptBase):
    """Модель для получения чека"""
    id: int
    created_at: datetime

    class Config:
        orm_mode = True


# Модель для результатов поиска
class ReceiptSearch(BaseModel):
    receipts: list[Receipt]
    total: int