#Imports
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

#Initialize App
app = FastAPI()
app.mount("/Frontend", StaticFiles(directory="../Frontend"), name="static")
templates = Jinja2Templates(directory="../Frontend")

##Different Post & Get Requests
#Home Page
@app.get("/home")
def get_index(request: Request):

    return templates.TemplateResponse(request=request, name="pages/index.html")