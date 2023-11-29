from fastapi import FastAPI, UploadFile, Form, Request, Response, File
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory='templates')

app = FastAPI(
    title='coupon-backend',
    version='0.1'
)


@app.get('/')
async def root(request: Request):
    return templates.TemplateResponse('coming_soon.html', {'request': request})

