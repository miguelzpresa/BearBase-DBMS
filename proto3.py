import rich 
from rich.prompt import Prompt
from rich.console import Console
from rich.table import Table
from rich import print
from rich import box
from rich import pretty
from rich import inspect
from rich import traceback




def opt(prompt,options,actionss:dict,tabla=None,sucursal=None)->None:
    while True:
        opt = Prompt.ask(prompt,choices=options)
        return opt
        if opt in actionss.keys():
            return actionss[opt]

        else:
            print("[red]Opción inválida[/]")

prompt2 = "[green]¿tipo de modificación?[/]"
options2 = ["(1)insert", "(2)update", "(3)delete", "(4)cancelar_operacion"]

prompt2_1 = "[green]¿En que tabla desea hacer la modificación?[/]"
options2_1 = ["Clientes", "Direcciones"]
actions2_1 = {
    "Clientes": "Clientes",
    "Direcciones": "Direcciones"
}

#print(actions2_1.keys())
tabla = opt(prompt2_1, options2_1, actions2_1)
print(tabla)
if 1 in actions2_1.keys():
    print("si")