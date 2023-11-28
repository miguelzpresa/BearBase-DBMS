import json
from json import load, dump
import threading
import pydantic
from pydantic import BaseModel, Field
import rich
from rich import print
from rich.table import Table
from rich.prompt import Prompt
import sys


from mariadb import connect, Error as MDBError

data = {}
cursors = []
connects = []

class Cliente(BaseModel):
    id_c: int = Field(..., ge=0)
    nombre: str
    apellido: str
    apellido_m: str
    rfc: str


class Direccion(BaseModel):
    id_d: int = Field(..., ge=0)
    calle: str
    numero: int = Field(..., ge=0)
    colonia: str
    estado: str
    cp: str
    id_c: int = Field(..., ge=0)
class Id_Manager():
    def __init__(self, bd, tabla):
        self.id_clients = 0 
        self.id_direcciones = 0
        self.bd = bd
        self.tabla = tabla
        self.get_id()

    def get_id(self,tabla):
        global cursors


        cursor = cursors[self.bd - 1]
        cursor.execute(f"SELECT MAX(id) FROM {self.tabla}")
        result = cursor.fetchone()
        last_id = result[0] if result[0] is not None else 0
        if self.tabla == "Clientes":
            self.id_clients = last_id + 1
        elif self.tabla == "Direcciones":
            self.id_direcciones = last_id + 1

        

    def __call__(self):
        return self.id
    def __repr__(self):
        return str(self.id)
    



def Init():
    global data
    file = open("./data.json", "r")
    data = load(file)
    file.close()

def Connection():
    global data, cursors, connects
    for i in data.keys():
        try:
            conn = connect(
                user=data[i]["User"],
                password=data[i]["Password"],
                host=data[i]["Host"],
                port=int(data[i]["Port"]),  # Convert to integer
                database=data[i]["Database"]
            )
            connects.append(conn)
            cursors.append(conn.cursor())
        except MDBError as e:
            print(f"[red]Error conectando a la base de datos:[/] {e}")
            sys.exit(1)

Init()
Connection()
print("[hot_pink1]Bienvenido![/]")
#print(cursors)
#print(connects)



def select(tablas,bd=1):#tablas=["clientes","Direcciones"]
    # si bd=1 es la primera base de datos, si bd=2 es la segunda, si bd=3 es las dos    
    global cursors
    results = []

    if bd==1 or bd==2:
        cursor=cursors[bd-1]
        
    elif bd==3:
        
        for cursor in cursors:
            for tabla in tablas:
                cursor.execute(f"SELECT * FROM {tabla}")
                results.extend(cursor.fetchall())
        return results
    for tabla in tablas:
        cursor.execute(f"SELECT * FROM {tabla}")
        results.extend(cursor.fetchall())
    return results

#print(select(tablas=["clientes"]))

def prompt_insert(tablas):
    
    if tablas == "Clientes":
        id_c = rich.input("[green]Ingrese el ID del cliente:[/]")
        #print(id_c)
        nombre = Prompt.ask("[green]Ingrese el nombre del cliente:[/]")
        apellido = Prompt.ask("[green]Ingrese el apellido paterno del cliente:[/]")
        apellido_m = Prompt.ask("[green]Ingrese el apellido materno del cliente:[/]")
        rfc = Prompt.ask("[green]Ingrese el RFC del cliente:[/]")
        return id_c,nombre,apellido,apellido_m,rfc
    elif tablas == "Direcciones":
        id_d = Prompt.ask("[green]Ingrese el ID de la dirección:[/]")
        calle = Prompt.ask("[green]Ingrese la calle:[/]")
        numero = Prompt.ask("[green]Ingrese el número de la calle:[/]")
        colonia = Prompt.ask("[green]Ingrese la colonia:[/]")
        estado = Prompt.ask("[green]Ingrese el estado:[/]")
        cp = Prompt.ask("[green]Ingrese el código postal:[/]")
        id_c = Prompt.ask("[green]Ingrese el ID del cliente:[/]")
        return id_d,calle,numero,colonia,estado,cp,id_c
from pydantic import BaseModel, Field

class Cliente(BaseModel):
    id_c: int = Field(..., ge=0)
    nombre: str
    apellido: str
    apellido_m: str
    rfc: str

class Direccion(BaseModel):
    id_d: int = Field(..., ge=0)
    calle: str
    numero: int = Field(..., ge=0)
    colonia: str
    estado: str
    cp: str
    id_c: int = Field(..., ge=0)

def prompt_insert(tablas):
    if tablas == "Clientes":
        cliente_data = Cliente(
            id_c=rich.input("[green]Ingrese el ID del cliente:[/]"),
            nombre=Prompt.ask("[green]Ingrese el nombre del cliente:[/]"),
            apellido=Prompt.ask("[green]Ingrese el apellido paterno del cliente:[/]"),
            apellido_m=Prompt.ask("[green]Ingrese el apellido materno del cliente:[/]"),
            rfc=Prompt.ask("[green]Ingrese el RFC del cliente:[/]")
        )
        return cliente_data.dict()
    elif tablas == "Direcciones":
        direccion_data = Direccion(
            id_d=Prompt.ask("[green]Ingrese el ID de la dirección:[/]"),
            calle=Prompt.ask("[green]Ingrese la calle:[/]"),
            numero=Prompt.ask("[green]Ingrese el número de la calle:[/]"),
            colonia=Prompt.ask("[green]Ingrese la colonia:[/]"),
            estado=Prompt.ask("[green]Ingrese el estado:[/]"),
            cp=Prompt.ask("[green]Ingrese el código postal:[/]"),
            id_c=Prompt.ask("[green]Ingrese el ID del cliente:[/]")
        )
        return direccion_data.dict()
def insert(tablas,bd,values):
    global cursors
    
    if tablas == "Clientes":

        cursor=cursors[bd-1]
        cursor.execute(f"INSERT INTO Clientes VALUES({values})")
        return cursor.fetchall()
    elif tablas == "Direcciones":
        id_d = Prompt.ask("[green]Ingrese el ID de la dirección:[/]")
        calle = Prompt.ask("[green]Ingrese la calle:[/]")
        numero = Prompt.ask("[green]Ingrese el número de la calle:[/]")
        colonia = Prompt.ask("[green]Ingrese la colonia:[/]")
        estado = Prompt.ask("[green]Ingrese el estado:[/]")
        cp = Prompt.ask("[green]Ingrese el código postal:[/]")
        id_c = Prompt.ask("[green]Ingrese el ID del cliente:[/]")
        cursor=cursors[bd-1]
        cursor.execute(f"INSERT INTO Direcciones VALUES({id_d},'{calle}',{numero},'{colonia}','{estado}',{cp},{id_c})")
        return cursor.fetchall()
    #if done:
        #print("[green]¡Datos insertados correctamente![/]")


print(prompt_insert(tablas=["clientes"]))


#print(insert(tablas=["clientes"], bd=1))
#rich.print(result)

