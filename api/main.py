from fastapi.openapi.docs import get_swagger_ui_html, get_redoc_html
from fastapi.responses import HTMLResponse

# Отключаем стандартные маршруты документации
app = FastAPI(
    title="Telegram Mini App API",
    description="API для работы с чеками в Telegram Mini App",
    version="1.0.0",
    docs_url=None,  # Отключаем стандартный /docs
    redoc_url=None  # Отключаем стандартный /redoc
)

# Создаем собственные маршруты документации
@app.get("/api/custom-docs", response_class=HTMLResponse)
async def get_custom_docs():
    return get_swagger_ui_html(
        openapi_url="/api/openapi.json",
        title="Telegram Mini App API",
        swagger_js_url="https://cdn.jsdelivr.net/npm/swagger-ui-dist@5/swagger-ui-bundle.js",
        swagger_css_url="https://cdn.jsdelivr.net/npm/swagger-ui-dist@5/swagger-ui.css"
    )