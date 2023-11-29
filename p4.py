import rich 
from rich.prompt import Prompt
from rich import print


def prompt_insert(tablas):
    
    if tablas == "Clientes":
        
        #print(id_c)
        error = False
        nombre = Prompt.ask("[green]Ingrese el nombre del cliente:[/]")
        for idxa in "1234567890.,-_:;{[´¨+*}] ¡¿?'=!)(/&%$#\"|)}":
            if idxa in nombre:
                error = True
        while error: 
            nombre = Prompt.ask("[red]Algun caracter no fue valido por favor vuelva a ingresar eñl nombre[/]")
            error = False
            for idxa in "1234567890.,-_:;{[´¨+*}] ¡¿?'=!)(/&%$#\"|)}":
                if idxa in nombre:
                    error = True
        apellido = Prompt.ask("[green]Ingrese el apellido paterno del cliente:[/]")
        apellido_m = Prompt.ask("[green]Ingrese el apellido materno del cliente:[/]")
        rfc = Prompt.ask("[green]Ingrese el RFC del cliente:[/]")
        return nombre,apellido,apellido_m,rfc
    elif tablas == "Direcciones":
        id_d = Prompt.ask("[green]Ingrese el ID de la dirección:[/]")
        calle = Prompt.ask("[green]Ingrese la calle:[/]")
        numero = Prompt.ask("[green]Ingrese el número de la calle:[/]")
        colonia = Prompt.ask("[green]Ingrese la colonia:[/]")
        estado = Prompt.ask("[green]Ingrese el estado:[/]")
        cp = Prompt.ask("[green]Ingrese el código postal:[/]")
        id_c = Prompt.ask("[green]Ingrese el ID del cliente:[/]")
        return id_d,calle,numero,colonia,estado,cp,id_c

print(prompt_insert("Clientes"))