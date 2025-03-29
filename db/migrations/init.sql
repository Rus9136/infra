-- Создание таблицы для хранения чеков
CREATE TABLE IF NOT EXISTS receipts (
    id SERIAL PRIMARY KEY,
    deleted_with_writeoff VARCHAR(20) NOT NULL,
    department VARCHAR(100) NOT NULL,
    dish_amount_int DECIMAL(15, 2) NOT NULL,
    dish_code VARCHAR(20) NOT NULL,
    dish_discount_sum_int DECIMAL(15, 2) NOT NULL,
    dish_measure_unit VARCHAR(10) NOT NULL,
    dish_name VARCHAR(200) NOT NULL,
    dish_sum_int DECIMAL(15, 2) NOT NULL,
    order_num INTEGER NOT NULL,
    pay_types VARCHAR(50) NOT NULL,
    precheque_time TIMESTAMP NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Создание индексов для оптимизации запросов (правильный синтаксис)
CREATE INDEX idx_department ON receipts(department);
CREATE INDEX idx_order_num ON receipts(order_num);
CREATE INDEX idx_pay_types ON receipts(pay_types);
CREATE INDEX idx_precheque_time ON receipts(precheque_time);

-- Добавление комментариев к таблице для документации
COMMENT ON TABLE receipts IS 'Таблица для хранения чеков из Telegram Mini App';
COMMENT ON COLUMN receipts.deleted_with_writeoff IS 'Статус удаления чека (NOT_DELETED и т.д.)';
COMMENT ON COLUMN receipts.department IS 'Название отдела или торговой точки';
COMMENT ON COLUMN receipts.dish_amount_int IS 'Количество товаров';
COMMENT ON COLUMN receipts.dish_code IS 'Код товара в системе';
COMMENT ON COLUMN receipts.dish_discount_sum_int IS 'Сумма скидки на товар';
COMMENT ON COLUMN receipts.dish_measure_unit IS 'Единица измерения товара';
COMMENT ON COLUMN receipts.dish_name IS 'Наименование товара';
COMMENT ON COLUMN receipts.dish_sum_int IS 'Сумма за товар';
COMMENT ON COLUMN receipts.order_num IS 'Номер заказа';
COMMENT ON COLUMN receipts.pay_types IS 'Способ оплаты';
COMMENT ON COLUMN receipts.precheque_time IS 'Время создания чека';