from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()

templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    tasks = [
        {"title": "Learn Azure", "status": "In Progress"},
        {"title": "Build Task Board", "status": "Completed"},
        {"title": "Deploy to Azure", "status": "Pending"},
    ]

    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={"tasks": tasks}
    )