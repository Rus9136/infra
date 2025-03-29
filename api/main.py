from fastapi import FastAPI
import uvicorn
from api.database import engine, Base

app = FastAPI(title="Madlen API")

# Импорт роутеров
from api.routers import router as main_router

# Создание таблиц в базе данных
Base.metadata.create_all(bind=engine)

# Подключение роутеров
app.include_router(main_router)

@app.get("/")
async def root():
    return {"message": "API работает!"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)