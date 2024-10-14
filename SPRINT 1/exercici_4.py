from typing import Union
from fastapi import FastAPI, Request
from pydantic import BaseModel, EmailStr
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates")
usuaris = []


# @app.get("/")
# def read_root():
#     return {"Hello":"World"}

# @app.get("/items/{items_id}")
# def read_item(items_id: int, q: Union[str, None] = None):
#     return {"item_id": items_id, "q": q}

class ActualitzarClient(BaseModel):  #DEFINIM LO MODEL QUE HEREDA DE BASE MODEL
    nom: str
    cognom: str
    edat: int
    email: EmailStr

@app.put("/usuaris/{user_id}")  #CREEM LA RUTA DEL PUT
def actualitztarUsuari(user_id: int, user: ActualitzarClient):   #DEFINIM FUNCIO DEFININT USERID COM INT I USER COM A LA CLASSE ANTERIOR.
    return {"user_id": user_id, "nom": user.nom, "cognom": user.cognom, "edat": user.edat, "email":user.email,  "missatge": "Usuari actualitzat correctament"}
# @app.post("/")
# CREAR ENDPOINT:
@app.post("/usuaris")
def crearUsuari(usuari: ActualitzarClient):  #funció que un usuari sigue el valor del model
    usuaris.append(usuari)  #afegim l'usuari dins de l'array global
    return {"missatge": "Usuari afegit correctament"}  # informem, ja que tot son json

@app.get("/usuaris")
def mostraUsuaris(request: Request):  #VARIABLE REQUEST TÉ VALOR DEL REQUEST DE FASTAPI 
    return templates.TemplateResponse("usuaris.html", {"request": request, "users":usuaris})  # REQUEST EL NECESSITA JINJA2 PARA FUNCIONAR PERO USUARIS ES EL VALRO DEL ARRAY..


@app.get("/usuaris/{user_id}")
def mostraDetallUsuari(user_id: int, request: Request):
    usuari = usuaris[user_id]
    return templates.TemplateResponse("usuari_complet.html", {"request": request, "usuari": usuari})
