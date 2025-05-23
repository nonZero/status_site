from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    host = request.headers.get("host", "???")
    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "host": host,
        },
    )
