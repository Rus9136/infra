const { Pool } = require('pg');

// Настройка подключения к PostgreSQL
const pool = new Pool({
  user: 'postgres',
  host: 'postgres', // имя сервиса в docker-compose
  database: 'telegram_miniapp_db',
  password: 'your_secure_password',
  port: 5432,
});

// Функция для сохранения чека в БД
async function saveReceipt(receiptData) {
  try {
    const client = await pool.connect();

    const query = `
      INSERT INTO receipts (
        deleted_with_writeoff, 
        department, 
        dish_amount_int, 
        dish_code, 
        dish_discount_sum_int, 
        dish_measure_unit, 
        dish_name, 
        dish_sum_int, 
        order_num, 
        pay_types, 
        precheque_time
      ) 
      VALUES ($1, $2, $3, $4, $5, $6, $7, $8, $9, $10, $11)
      RETURNING id
    `;

    const values = [
      receiptData.DeletedWithWriteoff,
      receiptData.Department,
      receiptData.DishAmountInt,
      receiptData.DishCode,
      receiptData.DishDiscountSumInt,
      receiptData.DishMeasureUnit,
      receiptData.DishName,
      receiptData.DishSumInt,
      receiptData.OrderNum,
      receiptData.PayTypes,
      receiptData.PrechequeTime
    ];

    const result = await client.query(query, values);
    client.release();

    return result.rows[0];
  } catch (err) {
    console.error('Ошибка при сохранении чека в базу данных:', err);
    throw err;
  }
}

module.exports = {
  saveReceipt,
  // Другие функции для работы с чеками...
};