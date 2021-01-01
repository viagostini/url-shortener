from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

origins = ["http://localhost:8080"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class Numero(BaseModel):
    valor: int


numero = Numero(valor=0)


class Shortlink(BaseModel):
    url: str


shortlink = Shortlink(url="")


@app.get("/shortlink")
def get_shortlink() -> dict:
    """Retorna o valor da variavel global :shortlink:"""
    global shortlink
    return {"shortlink": shortlink.url}


@app.post("/shortlink")
def update_shortlink(new_shortlink: Shortlink) -> dict:
    """Altera o valor da variavel global :shortlink: por :new_shortlink:"""
    global shortlink
    shortlink.url = new_shortlink
    return {"shortlink": shortlink.url}
