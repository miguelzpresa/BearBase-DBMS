#-----------#
# Bear Base #
#-----------#

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

def Update()->None:
    global data, cursors
    objetotipo = validator(Prompt.ask("[green]¿Que desea actualizar?[/] Cliente o Direccion",choices=["cliente","Direccion"]))
    idi = Prompt.ask("[green]Ingrese el ID[/]")
    if objetotipo == "cliente":
        nombre = validator(Prompt.ask("[green]Ingrese el nombre del cliente:[/]"))
        apellido = validator(Prompt.ask("[green]Ingrese el apellido paterno del cliente:[/]"))
        apellido_m = validator(Prompt.ask("[green]Ingrese el apellido materno del cliente:[/]"))
        rfc = validatorrfc(Prompt.ask("[green]Ingrese el RFC del cliente:[/]"))
        for i in cursors:
            i.execute(f"UPDATE clientes SET Nombre = '{nombre}', Ap_pat = '{apellido}', Ap_mat = '{apellido_m}', RFC = '{rfc}' WHERE ID = {idi}")
            i.commit()
    elif objetotipo == "Direccion":
        calle = Prompt.ask("[green]Ingrese la calle:[/]")
        numero = Prompt.ask("[green]Ingrese el número del domicilio:[/]")
        colonia = Prompt.ask("[green]Ingrese la colonia:[/]")
        estado = Prompt.ask("[green]Ingrese el estado:[/]")
        cp = Prompt.ask("[green]Ingrese el código postal:[/]")
        id_c = Prompt.ask("[green]Ingrese el ID del cliente:[/]")
        for i in cursors:
            i.execute(f"UPDATE Direcciones SET calle = '{calle}', numero = {numero}, colonia = '{colonia}', estado = '{estado}', CP = {cp}, clienteID = {id_c} WHERE ID = {idi}")
            i.commit()
    
        

def Search()->None:
    global data, cursors
    resultado = []
    tipobusqueda = Prompt.ask("[green]Por que desea buscar?[/] RFC, Nombre o Direccion",choices=["RFC", "Nombre", "Direccion"])
    if tipobusqueda == "RFC":
        rfc = validatorrfc(Prompt.ask("[green]Ingrese el RFC del cliente:[/]"))
        for i in cursors:
            i.execute(f"SELECT * FROM clientes WHERE RFC = '{rfc}'")
            if i.fetchall() != []:
                resultado.append(i.fetchall())
        if len(resultado) == 0:
            print("[red]No se encontraron resultados[/]")
        else:
            table = Table(title="Resultados de la busqueda")
            table.add_column("ID", justify="center", style="cyan")
            table.add_column("Nombre", justify="center", style="cyan")
            table.add_column("Apellido Paterno", justify="center", style="cyan")
            table.add_column("Apellido Materno", justify="center", style="cyan")
            table.add_column("RFC", justify="center", style="cyan")
            for i in resultado:
                for j in i:
                    table.add_row(str(j[0]), j[1], j[2], j[3], j[4])
            print(table)
    elif tipobusqueda == "Nombre":
        parte_de_nombre = Prompt.ask("[green]Ingrese si buscara por nombre, apellido paterno o apellido materno:[/]", options=["nombre", "apellido paterno", "apellido materno"])
        if parte_de_nombre == "nombre":
            nombre = validator(Prompt.ask("[green]Ingrese el nombre del cliente:[/]"))
            for i in cursors:
                i.execute(f"SELECT * FROM clientes WHERE Nombre = '{nombre}'")
                if i.fetchall() != []:
                    resultado.append(i.fetchall())
        elif parte_de_nombre == "apellido paterno":
            apellido = validator(Prompt.ask("[green]Ingrese el apellido paterno del cliente:[/]"))
            for i in cursors:
                i.execute(f"SELECT * FROM clientes WHERE Ap_pat = '{apellido}'")
                if i.fetchall() != []:
                    resultado.append(i.fetchall())
        elif parte_de_nombre == "apellido materno":
            apellido_m = validator(Prompt.ask("[green]Ingrese el apellido materno del cliente:[/]"))
            for i in cursors:
                i.execute(f"SELECT * FROM clientes WHERE Ap_mat = '{apellido_m}'")
                if i.fetchall() != []:
                    resultado.append(i.fetchall())
        if len(resultado) == 0:
            print("[red]No se encontraron resultados[/]")
        else:
            table = Table(title="Resultados de la busqueda")
            table.add_column("ID", justify="center", style="cyan")
            table.add_column("Nombre", justify="center", style="cyan")
            table.add_column("Apellido Paterno", justify="center", style="cyan")
            table.add_column("Apellido Materno", justify="center", style="cyan")
            table.add_column("RFC", justify="center", style="cyan")
            for i in resultado:
                for j in i:
                    table.add_row(str(j[0]), j[1], j[2], j[3], j[4])
            print(table)
    elif tipobusqueda == "Direccion":
        calle = Prompt.ask("[green]Ingrese la calle:[/]")
        numero = Prompt.ask("[green]Ingrese el número del domicilio:[/]")
        colonia = Prompt.ask("[green]Ingrese la colonia:[/]")
        estado = Prompt.ask("[green]Ingrese el estado:[/]")
        cp = Prompt.ask("[green]Ingrese el código postal:[/]")
        for i in cursors:
            i.execute(f"SELECT * FROM (clientes INNER JOIN Direcciones ON clientes.ID = Direcciones.clienteID) WHERE calle = '{calle}' AND numero = {numero} AND colonia = '{colonia}' AND estado = '{estado}' AND CP = {cp}") 
            if i.fetchall() != []:
                resultado.append(i.fetchall())
        if len(resultado) == 0:
            print("[red]No se encontraron resultados[/]")
        else:
            table = Table(title="Resultados de la busqueda")
            table.add_column("ID", justify="center", style="cyan")
            table.add_column("Nombre", justify="center", style="cyan")
            table.add_column("Apellido Paterno", justify="center", style="cyan")
            table.add_column("Apellido Materno", justify="center", style="cyan")
            table.add_column("RFC", justify="center", style="cyan")
            table.add_column("Calle", justify="center", style="cyan")
            table.add_column("Numero", justify="center", style="cyan")
            table.add_column("Colonia", justify="center", style="cyan")
            table.add_column("Estado", justify="center", style="cyan")
            table.add_column("CP", justify="center", style="cyan")
            for i in resultado:
                for j in i:
                    table.add_row(str(j[0]), j[1], j[2], j[3], j[4], j[5], str(j[6]), j[7], j[8], str(j[9]))
            print(table)
        
            

            



def validator(inputt:str):
    error = True
    while error:
        error = False
        for idx in "1234567890.,-!|@#$%&/()=?¡¿\"'\\ ":
            if idx in inputt:
                error = True
        if error:
            inputt = Prompt.ask("[red]Error, ingrese un valor válido sin caracteres especiales o espacios[/]")
    return inputt
                
def validatorrfc(inputt:str):
    error = True
    while error:
        error = False
        if len(inputt) != 13:
            error = True
        if error:
            inputt = Prompt.ask("[red]Error, ingrese un RFC valido[/]")
    return inputt

def num_validator(inputt):
    error = True
    while error:
        error = False
        for idx in inputt:
            if idx not in "1234567890":
                error = True
        if error:
            inputt = Prompt.ask("[red]Error, ingrese un campo valido[/]")

        
    return inputt  



    
def Insert()->None:
    global data, cursors
    sucursals = list(data.keys())
    suc = Prompt.ask("[green]¿En que sucursal desea insertar?[/]", choices=sucursals)
    
    cursor_a_usar = cursors[sucursals.index(suc)]
    tabla = Prompt.ask("[green]¿En que tabla desea insertar?[/]",choices=["clientes","Direcciones"])
    done = False
    if tabla == "clientes":
        nombre = validator(Prompt.ask("[green]Ingrese el nombre del cliente:[/]"))
        apellido = validator(Prompt.ask("[green]Ingrese el apellido paterno del cliente:[/]"))
        apellido_m = validator(Prompt.ask("[green]Ingrese el apellido materno del cliente:[/]"))
        rfc = validatorrfc(Prompt.ask("[green]Ingrese el RFC del cliente:[/]"))
        cursor_a_usar.execute(f"INSERT INTO clientes(Nombre,Ap_pat,Ap_mat,RFC) VALUES('{nombre}','{apellido}','{apellido_m}','{rfc}')")
        cursor_a_usar.commit()
        done = True
    elif tabla == "Direcciones":
        calle = validator(Prompt.ask("[green]Ingrese la calle:[/]"))
        numero = Prompt.ask("[green]Ingrese el número de la calle:[/]")
        colonia = validator(Prompt.ask("[green]Ingrese la colonia:[/]"))
        estado = validator(Prompt.ask("[green]Ingrese el estado:[/]"))
        cp = Prompt.ask("[green]Ingrese el código postal:[/]")
        id_c = Prompt.ask("[green]Ingrese el ID del cliente:[/]")# pendiente
        cursor_a_usar.execute(f"INSERT INTO Direcciones(calle,numero,colonia,estado,CP,clienteID) VALUES('{calle}',{numero},'{colonia}','{estado}',{cp},{id_c})")
        cursor_a_usar.commit()
        done = True
    if done:
        print("[green]¡Datos insertados correctamente![/]")
    else:
        print("[red]Error al insertar los datos[/]")

def Select():#tablas=["clientes","Direcciones"]
    global cursors, data

    bds = list(data.keys())
    bds.append("Todas")

    tabla = Prompt.ask("[green]¿Que tabla desea seleccionar?[/], Clientes, Direcciones o Ambas", choices=["clientes", "Direcciones", "Ambas"])
    base = Prompt.ask("[green]¿En que base de datos desea seleccionar?[/]", choices=bds)
    if tabla != "Ambas":
        tablas = [tabla]
    else:
        tablas = ["clientes", "Direcciones"]

    if base != "Todas":
        cursor=cursors[bds.index(base)]
        for tabla in tablas:
            cursor.execute(f"SELECT * FROM {tabla}")
            results = cursor.fetchall()
            if tabla == "Clientes":
                table = Table(title="Resultados de la busqueda")
                table.add_column("ID", justify="center", style="cyan")
                table.add_column("Nombre", justify="center", style="cyan")
                table.add_column("Apellido Paterno", justify="center", style="cyan")
                table.add_column("Apellido Materno", justify="center", style="cyan")
                table.add_column("RFC", justify="center", style="cyan")
                for i in results:
                    table.add_row(str(i[0]), i[1], i[2], i[3], i[4])
            elif tabla == "Direcciones":
                table = Table(title="Resultados de la busqueda")
                table.add_column("ID", justify="center", style="cyan")
                table.add_column("Calle", justify="center", style="cyan")
                table.add_column("Numero", justify="center", style="cyan")
                table.add_column("Colonia", justify="center", style="cyan")
                table.add_column("Estado", justify="center", style="cyan")
                table.add_column("CP", justify="center", style="cyan")
                table.add_column("ID Cliente", justify="center", style="cyan")
                for i in results:
                    table.add_row(str(i[0]), i[1], i[2], i[3], i[4], i[5], str(i[6]))
    elif base =="Todas":
        for cursore in list(data.keys()):
            print(f"[cyan]Base de datos {cursore}[/]")
            cursor = cursors[list(data.keys()).index(cursore)]
            for tabla in tablas:
                cursor.execute(f"SELECT * FROM {tabla}")
                results.extend(cursor.fetchall())
                if tabla == "clientes":
                    table = Table(title="Resultados de la busqueda")
                    table.add_column("ID", justify="center", style="cyan")
                    table.add_column("Nombre", justify="center", style="cyan")
                    table.add_column("Apellido Paterno", justify="center", style="cyan")
                    table.add_column("Apellido Materno", justify="center", style="cyan")
                    table.add_column("RFC", justify="center", style="cyan")
                    for i in results:
                        table.add_row(str(i[0]), i[1], i[2], i[3], i[4])
                elif tabla == "Direcciones":
                    table = Table(title="Resultados de la busqueda")
                    table.add_column("ID", justify="center", style="cyan")
                    table.add_column("Calle", justify="center", style="cyan")
                    table.add_column("Numero", justify="center", style="cyan")
                    table.add_column("Colonia", justify="center", style="cyan")
                    table.add_column("Estado", justify="center", style="cyan")
                    table.add_column("CP", justify="center", style="cyan")
                    table.add_column("ID Cliente", justify="center", style="cyan")
                    for i in results:
                        table.add_row(str(i[0]), i[1], i[2], i[3], i[4], i[5], str(i[6]))
        

              

def Connection():
    global data, cursors, connects
    for i in data.keys():
        try:
            conn = connect(
                user=data[i]["User"],
                password=data[i]["Password"],
                host=data[i]["Host"],
                port=int(data[i]["Port"]),
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
        r = Prompt.ask("¿Qué desea hacer?", choices=["Actualizar", "Buscar", "Insertar","Seleccionar", "Salir" ])
        if r == "Insertar":
            Insert()
        elif r == "Buscar":
            Search()
        elif r == "Seleccionar":
            Select()
        elif r == "Actualizar":
            Update()
        elif r == "Salir":
            in_app = False
            print("[hot_pink1]Saliendo...[/]")
            Poweroff()
main()