import npyscreen
import sys
sys.path.append("..")
from os import system
from view.interface import CreateInterface

def startView():
    try:
        npyscreen.wrapper(CreateInterface().run())
    except ValueError:
        system('cls')
        print("|ERROR| Invalid image format.")
        exit()
    except AttributeError:
        system('cls')
        print("|AVISO| Imagem processada com sucesso")
        pass

startView()