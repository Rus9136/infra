from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.openapi.utils import get_openapi
import uvicorn

from database import engine, Base
from routers import receipts

# Создание таблиц в БД (если они еще не существуют)
Base.metadata.create_all(bind=engine)

# Создание экземпляра FastAPI (оставляем основные параметры)
app = FastAPI(
    title="Telegram Mini App API",
    description="API для работы с чеками в Telegram Mini App",
    version="1.0.0"
)

# Добавление функции для настройки OpenAPI схемы
def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="Telegram Mini App API",
        version="1.0.0",
        description="API для работы с чеками в Telegram Mini App",
        routes=app.routes,
    )
    # Задаем явно версию OpenAPI
    openapi_schema["openapi"] = "3.0.2"
    app.openapi_schema = openapi_schema
    return app.openapi_schema

# Заменяем стандартную схему OpenAPI на нашу
app.openapi = custom_openapi

# Настройка CORS для доступа из веб-приложения
origins = [
    "http://localhost",
    "http://localhost:8080",
    "https://madlen.space",
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