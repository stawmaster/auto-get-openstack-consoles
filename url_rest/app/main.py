from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from app.db.models import Request
from app.api import api

app = FastAPI()


@app.get("/")
def root():
    return {"message": "This is the root of the RESTful API of the auto access tool , visit /help for more info"}

@app.get("/help")
def help():
    return {"help"      : "Here's a list of the templating engine's functionalities. descriptions starting with * mean that the corresponding request requires a body",
            "/"         : "Root page",
            "/help"     : "You are right here !",
            "/howto"    : "How to use the templating engine"}

@app.get("/howto")
def howto():
    return {"howto": "test"}

@app.get("/refresh")
def read_consoles():
    return api.read_consoles()


@app.post("/request", status_code=200)
def respond(payload: Request):
    payload = payload.dict()

    return api.respond(payload)


