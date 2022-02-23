import click, colorama
from colorama import Fore, Back, Style
from art import text2art
import modulos as HAL
import gui_orbitas as GUI
colorama.init(autoreset=True)

def pantalla_inicial():
    click.clear()
    texto =text2art("GUA",font='block',chr_ignore=True)
    subtitulo=text2art("Astro Tool Kit")
    print(f"{Fore.LIGHTYELLOW_EX}{texto}")
    print(f"{subtitulo}")
    print(f"{Fore.RED}Programado por: Santiago Acuña G.")
    print(f"{Fore.RED}Hecho para Mecánica de Vuelo Espacial por Juan José Mejía")
    print(f"{Fore.RED}V 1.01")
    click.pause()
    click.clear()

def menu():
    click.clear()
    eleccion=None
    while eleccion!="EXIT":
        click.clear()
        opciones = ["1. Calculadora para solución numérica ejemplo 4.3","2. Graficador de Órbitas"]
        nombre_menu = text2art("menu",font="smslant")
        click.echo(f"{Fore.LIGHTYELLOW_EX} {nombre_menu}")
        for n in opciones:
            print(f"{Fore.WHITE}{n}\n")
        eleccion=click.prompt(
            f"{Fore.YELLOW}Seleccione la opción que le interese con el número respectivo \n Para salir escriba EXIT"
        )
        if eleccion.lower() == "exit":
            return None
        else:
            numero = 900000
            try:
                numero=int(eleccion)
            except:
                click.echo(f"{Fore.LIGHTRED_EX} LA SELECCIÓN ES INVÁLIDA, INTENTE DE NUEVO")
                click.pause()
            if numero == 1:
                click.clear()
                subtitulo=text2art("Astro Tool Kit")
                print(subtitulo)
                click.echo(f"Bienvenido a la Calculadora para solución numérica ejemplo 4.3\nPara este programa puede elegir usar los datos default del ejemplo o usar los que usted desée")
                print("\n")
                click.pause()
                choice=click.prompt("Escriba 1 si quiere usar sus propios datos y escriba 2 si quiere usar los usados en el problema")
                resultado=HAL.calcular_masa_total_minima_launch(int(choice))
                print(f"{Fore.LIGHTRED_EX}El resultado calculado es el siguiente: {round(resultado,3)} kg")
                click.pause()
            elif numero == 2:
                click.clear()
                subtitulo=text2art("Astro Tool Kit")
                print(subtitulo)
                click.echo(f"{Fore.YELLOW}Bievenido al Graficador de Órbitas!!\n")
                click.pause()
                click.echo("Abriendo la GUI, Por favor espere......")
                GUI.GUI()


                    

pantalla_inicial()
menu()