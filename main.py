from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from data import produto_repo
import uvicorn


app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")
produto_repo.criar_tabela()



@app.get("/")
async def root():
    protudos = produto_repo.obter_todos()
    response = templates.TemplateResponse("index.html", {"request": {}, "produtos": protudos})
    return response


if __name__ == "__main__":
    uvicorn.run(app="main:app", host="127.0.0.1", port=8000, reload=True)