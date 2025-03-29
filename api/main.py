from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

from database import engine, Base
from routers import receipts

# Создание таблиц в БД (если они еще не существуют)
Base.metadata.create_all(bind=engine)

# Создание экземпляра FastAPI
# Нужно изменить на:
app = FastAPI(
    title="Telegram Mini App API",
    description="API для работы с чеками в Telegram Mini App",
    version="1.0.0",
    openapi_version="3.1.0"  # Добавить эту строку
)
# Настройка CORS для доступа из веб-приложения
origins = [
    "http://localhost",
    "http://localhost:8080",
    "https://ваш-домен.ru",  # Замените на ваш домен
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Подключение роутеров
app.include_router(receipts.router)

# Корневой маршрут
@app.get("/")
async def root():
    return {"message": "Telegram Mini App API работает! Документация доступна по адресу /docs"}

# Для локального запуска (при разработке)
if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)