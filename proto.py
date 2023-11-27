import mariadb
import rich
import json
from mariadb import connect, Error as MDBError
from rich import print
from rich.table import Table
from rich.prompt import Prompt
from json import load, dump
import sys


# Variables & Objects

in_app = True
data = {}
cursors = []
connects = []
query = ""

# Functions

def Init():
    global data
    file = open("./data.json", "r")
    data = load(file)
    file.close()

def opt(prompt,options,actionss:dict,tabla=None,sucursal=None)->None:
    while True:
        opt = Prompt.ask(prompt,choices=options)
        if opt in actionss.keys():
            try:    return actionss[opt](tabla,sucursal)
            except Exception: return actionss[opt]

        else:
            print("[red]Opción inválida[/]")




def home()->None:
    global query
    query = ""
    promp1= "Opciones"
    choices1=["(1)Listar", "(2)Buscar", "(3)modificar", "(4)Salir"]
    actions1= {
        1: Select(),
        2: Search(),
        3: Modi(),
        4: Poweroff()
    }
    opt(promp1,choices1,actions1)
def tabla(tabla)->None:
    global query
    query.append(tabla)


def Select(tabla=None,sucursal=None)->bool:
    pass

def Update(tabla=None,sucursal=None)->bool:
    pass

import json

def Search(tabla=None, sucursal=None) -> bool:
    pass

def Insert(tabla=None, sucursal=None) -> bool:
    done = False
    if tabla == "Clientes":
        id_c = Prompt.ask("[green]Ingrese el ID del cliente:[/]")
        nombre = Prompt.ask("[green]Ingrese el nombre del cliente:[/]")
        apellido = Prompt.ask("[green]Ingrese el apellido paterno del cliente:[/]")
        apellido_m = Prompt.ask("[green]Ingrese el apellido materno del cliente:[/]")
        rfc = Prompt.ask("[green]Ingrese el RFC del cliente:[/]")
        cursor_a_usar.execute(f"INSERT INTO Clientes VALUES({id_c},'{nombre}','{apellido}','{apellido_m}','{rfc}')")
        done = True
    elif tabla == "Direcciones":
        id_d = Prompt.ask("[green]Ingrese el ID de la dirección:[/]")
        calle = Prompt.ask("[green]Ingrese la calle:[/]")
        numero = Prompt.ask("[green]Ingrese el número de la calle:[/]")
        colonia = Prompt.ask("[green]Ingrese la colonia:[/]")
        estado = Prompt.ask("[green]Ingrese el estado:[/]")
        cp = Prompt.ask("[green]Ingrese el código postal:[/]")
        id_c = Prompt.ask("[green]Ingrese el ID del cliente:[/]")
        cursor_a_usar = connect().cursor()  # Define the cursor_a_usar variable
        cursor_a_usar.execute(f"INSERT INTO Direcciones VALUES({id_d},'{calle}',{numero},'{colonia}','{estado}',{cp},{id_c})")
        done = True
    if done:
        print("[green]¡Datos insertados correctamente![/]")

def Delete(tabla=None, sucursal=None) -> bool:
    pass

def Modi() -> bool:
    global data, cursors, query
    query = ""

    sucursals = list(data.keys())

    prompt2 = "[green]¿tipo de modificación?[/]"
    options2 = ["(1)insert", "(2)update", "(3)delete", "(4)cancelar_operacion"]

    prompt2_1 = "[green]¿En que tabla desea hacer la modificación?[/]"
    options2_1 = ["(1)Clientes", "(2)Direcciones"]
    actions2_1 = {
        1: "Clientes",
        2: "Direcciones"
    }

    prompt2_2 = "[green]¿En que sucursal desea hacer la modificación?[/]"
    options2_2 = ["(1)Sucursal 1", "(2)Sucursal 2"]
    actions2_2 = {
        1: cursors[sucursals.index(0)],
        2: cursors[sucursals.index(1)]
    }

    tabla = opt(prompt2_1, options2_1, actions2_1)

    actions2 = {
        1: Insert(tabla=None),
        2: Update(tabla=None),
        3: Delete(tabla=None),
        4: home()
    }
    modo = opt(prompt2, options2, actions2, tabla)

    query.append(modo)

    suc = Prompt.ask("[green]¿Modificación simple/granulada ?[/]", choices=sucursals)
    cursor_a_usar = cursors[sucursals.index(suc)]

  


        

def Connection():
    global data, cursors, connects
    for i in data.keys():
        try:
            conn = connect(
                user=data[i]["User"],
                password=data[i]["Password"],
                host=data[i]["Host"],
                port=data[i]["Port"],
                database=data[i]["Database"]
            )
            connects.append(conn)
            cursors.append(conn.cursor())
        except MDBError as e:
            print(f"[red]Error conectando a la base de datos:[/] {e}")
            sys.exit(1)

def Poweroff():
    global connects, in_app
    in_app = False
    print("[hot_pink1]Saliendo...[/]")
    for i in connects:
        i.close()

# Main

# Read data from data.json
with open("data.json") as file:
    data = json.load(file)

# Call Connection function
Connection()


def main()->None:

    global in_app
    Init()
    print(data)
    return 0
    Connection()
    print("[hot_pink1]Bienvenido![/]")
    while in_app:
        home()

   

if __name__ == "__main__":
    main()