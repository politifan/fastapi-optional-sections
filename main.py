import os
from pathlib import Path

from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from starlette.requests import Request

app = FastAPI(title="FastAPI Optional Sections")
templates = Jinja2Templates(directory=Path(__file__).parent / "templates")


@app.get("/", response_class=HTMLResponse)
def homepage(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={
            "announcement": os.getenv("SITE_ANNOUNCEMENT", "").strip(),
            "contact": os.getenv("SITE_CONTACT", "").strip(),
        },
    )
