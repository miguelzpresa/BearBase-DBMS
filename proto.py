#-----------#
# Bear Base #
#-----------#
#PSEUDCODGIGO






# Imports


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

# Functions
def Init():
    global data
    file = open("data.json", "r")
    data = load(file)
    file.close()

def Update()->bool:
    pass

def Search()->bool:
    pass

def Insert()->bool:
    global data, cursors
    sucursals = list(data.keys())
    suc = Prompt.ask("[green]¿En que sucursal desea insertar?[/]", choices=sucursals)
    cursor_a_usar = cursors[sucursals.index(suc)]
    tabla = Prompt.ask("[green]¿En que tabla desea insertar?[/]",choices=["Clientes","Direcciones"])
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
        cursor_a_usar.execute(f"INSERT INTO Direcciones VALUES({id_d},'{calle}',{numero},'{colonia}','{estado}',{cp},{id_c})")
        done = True
    if done:
        print("[green]¡Datos insertados correctamente![/]")

        

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
    global connects
    for i in connects:
        i.close()
# Main

def main()->None:
    global in_app
    Init()
    Connection()
    while in_app:
        r = Prompt.ask("¿Qué desea hacer?", choices=["Actualizar", "Buscar", "Insertar", "Salir"])
        if r == "Insertar":
            Insert()
        elif r == "Salir":
            in_app = False
            print("[hot_pink1]Saliendo...[/]")
            Poweroff()

