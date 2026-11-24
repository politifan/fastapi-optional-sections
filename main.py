import mimetypes
import os
from pathlib import Path

from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from starlette.requests import Request

BASE_DIR = Path(__file__).resolve().parent
mimetypes.add_type("image/webp", ".webp")
app = FastAPI(title="Один день")
app.mount("/static", StaticFiles(directory=BASE_DIR / "static"), name="static")
templates = Jinja2Templates(directory=BASE_DIR / "templates")

CHAPTERS = (
    {
        "city": "Эдинбург",
        "label": "ПЕРВАЯ ВСТРЕЧА",
        "image": "edinburgh.webp",
        "text": "15 июля 1988 года. Университет позади, планы на жизнь ещё можно изменить. В эту ночь Эмма и Декстер наконец разговаривают.",
    },
    {
        "city": "Лондон",
        "label": "В РАЗНЫЕ СТОРОНЫ",
        "image": "london.webp",
        "text": "Эмма ищет своё место и продолжает писать. Декстер оказывается в мире телевидения. У каждого свой ритм, и всё труднее поймать момент, чтобы поговорить.",
    },
    {
        "city": "Париж",
        "label": "СНОВА ВМЕСТЕ",
        "image": "paris.webp",
        "text": "Эмма пишет в Париже, когда туда приезжает Декстер. После стольких лет им предстоит решить, что делать с чувствами, о которых они долго молчали.",
    },
)


@app.get("/", response_class=HTMLResponse)
def homepage(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={
            "chapters": CHAPTERS,
            "announcement": os.getenv("SITE_ANNOUNCEMENT", "").strip(),
            "contact": os.getenv("SITE_CONTACT", "").strip(),
        },
    )
