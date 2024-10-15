from typing import Union
from fastapi import FastAPI, Request
from pydantic import BaseModel, EmailStr
from fastapi.templating import Jinja2Templates
templates = Jinja2Templates(directory="templates_training")

application_training = FastAPI()
# POST
# GET
# PUT

productes = []
class Producte(BaseModel):
    name: str
    price: float
    quantity: int
    desc: str

@application_training.post("/productes")
def afegirProductes(producte: Producte):
    productes.append(producte)
    return {"missatge": "Producte afegit correctament"}

@application_training.get("/productes")
def mostraProductes(request: Request):
 return templates.TemplateResponse("productes.html", {"request": request, "productes": productes})


@application_training.put("/productes/{product_id}")
def actualitzarProducte(product_id: int, producte: Producte):
    if product_id >= len(productes) or product_id < 0:
        return {"error": "Producte no trobat"}
    productes[product_id] = producte
    return {"missatge:": "Producte actualitzat."}

@application_training.get("/productes/{product_id}")
def mostrarProducte(product_id: int, request: Request):
   producte = productes[product_id]
   return templates.TemplateResponse("producte_full.html", {"request":request, "producte": producte})
