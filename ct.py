# Import the necessary packages
import sys
from consolemenu import *
from consolemenu.items import *
from consolemenu.items import FunctionItem, SubmenuItem, CommandItem
import sys
import os
import shutil

#Functions
def lista(): 
    pat = os.getcwd()
    # Get the list of all files and directories
    fp = pat
    dir_list = os.listdir(fp)
    print("Files and directories in '", fp, "' :")
    # prints all files
    print(dir_list)


def delt(): 
     pat = os.getcwd()
     canonfolder = input
     shutil.rmtree(canonfolder)

def nowfile(): 
     pat = os.getcwd()
     fp = input
     print("Digita o que vai ser escrito no ficheiro. Ctrl-D or Ctrl-Z para terminar")
     contents = []
     while True:
         try:
             line = input()
         except EOFError:
             break
         contents.append(line)
     txt = input()
     fil = pat+fp
     with open(fil,"w") as file:
         file.writelines(contents)


def printfile(): 
    pat = os.getcwd()
    fil = input
    fpfile = open(fil, "r")
    print ("ficheiro aberto")
    content_list = fpfile.readlines()
    print ("ficheiro fechado")
    print(content_list)


def afile(): 
    pat = os.getcwd
    fp = input
    print("Digita o que vai ser escrito no ficheiro. Ctrl-D or Ctrl-Z para terminar")
    contents = []
    while True:
        try:
            line = input()
        except EOFError:
            break
        contents.append(line)
    txt = input()
    fil = pat+fp
    with open(fil,"a") as file:
        file.writelines(contents)
        
def ot(): 
    exit()        


#Menu
menu = ConsoleMenu("Menu Principal", "Welcome to the fricking jungle!!!")
# Create some items

function_one = FunctionItem("Lista", lista)
function_two = FunctionItem("Elimina",delt)
function_three = FunctionItem("Cria", nowfile)
function_four = FunctionItem("Sai", ot)
subfunctionone = FunctionItem("abrir",)
subfunctiontwo = FunctionItem("Criar",nowfile)
subfunctionthree = FunctionItem("apagar",delt)
subfunctionfour = FunctionItem("eliminar dados",afile)
subfunctionfive = FunctionItem("acrescentar dados",afile)
subfunctionsix = FunctionItem("sair",quit())

#add menu items
menu.append_item(function_one)
submenu = ConsoleMenu("Listar Ficheiros")
submenu_item_one = SubmenuItem("Abrir", submenu, menu=menu)
submenu_item_two = SubmenuItem("Criar", submenu, menu=menu)
submenu_item_three = SubmenuItem("Eliminar", submenu, menu=menu)
submenu_item_four = SubmenuItem("Eliminar Dados", submenu, menu=menu)
submenu_item_five = SubmenuItem("Acrescentar Dados", submenu, menu=menu)
submenu_item_six = SubmenuItem("Menu Anterior", submenu, menu=menu)
menu.append_item(submenu_item_one, subfunctionone)
menu.append_item(submenu_item_two, subfunctiontwo)
menu.append_item(submenu_item_three, subfunctionthree)
menu.append_item(submenu_item_four, subfunctionfour)
menu.append_item(submenu_item_five, subfunctionfive)
menu.append_item(submenu_item_six, subfunctionsix)


menu.append_item(function_two)
menu.append_item(function_three)
menu.append_item(function_four)


#display menu
menu.show()