# pip install fastapi uvicorn
# uvicorn fast:app --reload

from fastapi import FastAPI

app = FastAPI()

vendas = {
    1: {"item": 'lata', "preco_unitario": 4, "quantidade": 5},
    2: {"item": 'garrafa', "preco_unitario": 15, "quantidade": 5},
    3: {"item": 'lata mini', "preco_unitario": 2, "quantidade": 5},
}

@app.get('/')
def home():
    return {"vendas": len(vendas)}

@app.get("/vendas/{id_venda}")
def pegar_venda(id_venda:int):
    return {'venda': vendas.get(id_venda)}