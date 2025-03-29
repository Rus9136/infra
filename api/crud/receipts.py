from sqlalchemy.orm import Session
from sqlalchemy import desc
from models.receipt import ReceiptDB, ReceiptCreate, Receipt
from datetime import datetime
from typing import Optional, List, Dict, Any


# Получить все чеки с пагинацией
def get_receipts(db: Session, skip: int = 0, limit: int = 100):
    total = db.query(ReceiptDB).count()
    receipts = db.query(ReceiptDB).order_by(desc(ReceiptDB.precheque_time)).offset(skip).limit(limit).all()
    return {"receipts": receipts, "total": total}


# Получить чек по ID
def get_receipt(db: Session, receipt_id: int):
    return db.query(ReceiptDB).filter(ReceiptDB.id == receipt_id).first()


# Получить чеки по номеру заказа
def get_receipts_by_order_num(db: Session, order_num: int):
    return db.query(ReceiptDB).filter(ReceiptDB.order_num == order_num).all()


# Получить чеки по параметрам (фильтрация)
def get_receipts_by_filters(db: Session, filters: Dict[str, Any], skip: int = 0, limit: int = 100):
    query = db.query(ReceiptDB)

    if "department" in filters and filters["department"]:
        query = query.filter(ReceiptDB.department == filters["department"])

    if "pay_types" in filters and filters["pay_types"]:
        query = query.filter(ReceiptDB.pay_types == filters["pay_types"])

    if "date_from" in filters and filters["date_from"]:
        query = query.filter(ReceiptDB.precheque_time >= filters["date_from"])

    if "date_to" in filters and filters["date_to"]:
        query = query.filter(ReceiptDB.precheque_time <= filters["date_to"])

    if "order_num" in filters and filters["order_num"]:
        query = query.filter(ReceiptDB.order_num == filters["order_num"])

    total = query.count()
    receipts = query.order_by(desc(ReceiptDB.precheque_time)).offset(skip).limit(limit).all()

    return {"receipts": receipts, "total": total}


# Создать новый чек
def create_receipt(db: Session, receipt: ReceiptCreate):
    db_receipt = ReceiptDB(
        deleted_with_writeoff=receipt.deleted_with_writeoff,
        department=receipt.department,
        dish_amount_int=receipt.dish_amount_int,
        dish_code=receipt.dish_code,
        dish_discount_sum_int=receipt.dish_discount_sum_int,
        dish_measure_unit=receipt.dish_measure_unit,
        dish_name=receipt.dish_name,
        dish_sum_int=receipt.dish_sum_int,
        order_num=receipt.order_num,
        pay_types=receipt.pay_types,
        precheque_time=receipt.precheque_time
    )
    db.add(db_receipt)
    db.commit()
    db.refresh(db_receipt)
    return db_receipt


# Удалить чек
def delete_receipt(db: Session, receipt_id: int):
    receipt = db.query(ReceiptDB).filter(ReceiptDB.id == receipt_id).first()
    if receipt:
        db.delete(receipt)
        db.commit()
        return True
    return False