from fastapi import FastAPI
from opentelemetry.instrumentation.requests import RequestsInstrumentor
from opentelemetry.instrumentation.fastapi import FastAPIInstrumentor
from utils import initialize_telemetry
from settings import settings
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi import Request

initialize_telemetry()

RequestsInstrumentor().instrument()
templates = Jinja2Templates(directory="templates")

app = FastAPI(
    title=settings.PROJECT_NAME,
    description=settings.PROJECT_DESCRIPTION,
    version=settings.PROJECT_VERSION
)

FastAPIInstrumentor.instrument_app(app)

@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.get("/", response_class=HTMLResponse, include_in_schema=False)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {
        "request": request,
        "project_name": settings.PROJECT_NAME,
        "version": settings.PROJECT_VERSION,
        "author": settings.PROJECT_AUTHOR,
        "profile_image_url": settings.PROJECT_AUTHOR_IMAGE_URL
    })
