from fastapi import Form
from fastapi import Request
from backup.tmp.tutorial import app
from backup.tmp.tutorial import templates
from fastapi.responses import HTMLResponse
from pydantic import BaseModel


class User(BaseModel):
    id: int
    username: str
    email: str


class Logpass(BaseModel):
    username: str
    password: str


@app.get("/form")
def form_post(request: Request):
    result = "Type a number"
    return templates.TemplateResponse('template.html', context={'request': request, 'result': result})


@app.post("/form")
def form_post(request: Request, username: str = Form(...), password: str = Form(...)):
    result = 123
    return templates.TemplateResponse('template.html', context={'request': request, 'result': result, 'num': 123})


@app.get("/form/1")
def form_post2(request: Request, username: str, password: str):
    return templates.TemplateResponse('test2.html',
                                      context={'request': request, 'username': username, 'password': password})


@app.get("/form/1")
def form_post(request: Request, username: str = Form(...), password: str = Form(...)):
    return templates.TemplateResponse('test2.html',
                                      context={'request': request, 'username': username, 'password': password})


@app.post("/form/1")
def form_post(request: Request, username: str = Form(...), password: str = Form(...)):
    return templates.TemplateResponse('test2.html',
                                      context={'request': request, 'username': username, 'password': password})


@app.get("/form2")
def form_post(request: Request):
    result = "Type a number"
    return templates.TemplateResponse('template3.html', context={'request': request, 'result': result})


@app.post("/form2")
def form_post(request: Request, username: str = Form(...), password: str = Form(...)):
    result = 123
    response = templates.TemplateResponse('template3.html', context={'request': request, 'result': result, 'num': 123})
    return response


@app.get("/html/", response_class=HTMLResponse)
async def read_items():
    html_content = """
    <!doctype html>
    <head><title>Test</title> 
    <meta charset=utf-8> </head>
    <body>
        <h1>My Website</h1>
        <form action="/my-link/">
            <input type="submit" value="Click me" />
        </form>    
        <button> <a href="/my-link/">Click me</a></button>
    </body>
    """
    return HTMLResponse(content=html_content, status_code=200)


@app.post("/user")
def main(username: User):
    return {"key": username}


@app.get("/user/{user_id}", response_model=User)
def main(user_id: int):
    user = {"id": 55, "username": "Ivan", "email": "siv@mail.ru"}
    return user
