from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI () 

#medelo de datos Reserva

class Reserva(BaseModel):
    id_reserva: int
    id_sala: int
    id_usuario: int
    fecha: str
    hora_inicio: str
    hora_fin: str
    personas: int
    estado: str

reservas = [] # Lista para base de datos temporal 



#Creacion del endpoint post/reservas
@app.post("/reservas")
def crear_reservas(reserva: Reserva):
    reservas.append(reserva)
    return {"mensaje": "Reserva creada exitosamente", "reserva": reserva}   

#Creacion del endpoint Get/reservas
@app.get("/reservas")
def obtener_reservas():
    return {"reservas": reservas}          
