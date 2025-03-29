from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import List, Optional
from datetime import datetime

from database import get_db
from models.receipt import Receipt, ReceiptCreate, ReceiptSearch
import crud.receipts as crud

router = APIRouter(
    prefix="/receipts",
    tags=["receipts"],
    responses={404: {"description": "Not found"}},
)


@router.post("/", response_model=Receipt)
def create_receipt(receipt: ReceiptCreate, db: Session = Depends(get_db)):
    """
    Создать новый чек
    """
    return crud.create_receipt(db=db, receipt=receipt)


@router.get("/", response_model=ReceiptSearch)
def read_receipts(
        skip: int = 0,
        limit: int = 100,
        department: Optional[str] = None,
        pay_types: Optional[str] = None,
        order_num: Optional[int] = None,
        date_from: Optional[datetime] = None,
        date_to: Optional[datetime] = None,
        db: Session = Depends(get_db)
):
    """
    Получить список чеков с фильтрацией
    """
    filters = {
        "department": department,
        "pay_types": pay_types,
        "order_num": order_num,
        "date_from": date_from,
        "date_to": date_to
    }
    # Удаляем None значения
    filters = {k: v for k, v in filters.items() if v is not None}

    if filters:
        return crud.get_receipts_by_filters(db, filters=filters, skip=skip, limit=limit)
    else:
        return crud.get_receipts(db, skip=skip, limit=limit)


@router.get("/{receipt_id}", response_model=Receipt)
def read_receipt(receipt_id: int, db: Session = Depends(get_db)):
    """
    Получить чек по ID
    """
    db_receipt = crud.get_receipt(db, receipt_id=receipt_id)
    if db_receipt is None:
        raise HTTPException(status_code=404, detail="Receipt not found")
    return db_receipt


@router.get("/order/{order_num}", response_model=List[Receipt])
def read_receipts_by_order(order_num: int, db: Session = Depends(get_db)):
    """
    Получить чеки по номеру заказа
    """
    receipts = crud.get_receipts_by_order_num(db, order_num=order_num)
    return receipts


@router.delete("/{receipt_id}", response_model=bool)
def delete_receipt(receipt_id: int, db: Session = Depends(get_db)):
    """
    Удалить чек по ID
    """
    result = crud.delete_receipt(db, receipt_id=receipt_id)
    if not result:
        raise HTTPException(status_code=404, detail="Receipt not found")
    return result