
from optparse import Option
import os
 
 
def listdir(pat, ext): 
    # Get the list of all files and directories
    fp = pat+ext
    dir_list = os.listdir(fp)
    print("Files and directories in '", fp, "' :")
    # prints all files
    print(dir_list)

def printfile(pat, fp): 
    fil = pat+fp
    fpfile = open(fil, "r")
    print ("ficheiro aberto")
    content_list = fpfile.readlines()
    print ("ficheiro fechado")
    print(content_list)

def nowfile(pat, fp): 
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

def afile(pat, fp): 
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


menu_options = {
    1: 'Listar ficheiros',
    2: 'Abrir ficheiro',
    3: 'Escrever ou criar novo ficheiro',
    4: 'Adicionar conteudo ao ficheiro',
    5: 'Sair',
}

def print_menu():
    for key in menu_options.keys():
        print (key, '--', menu_options[key] )
    
    
    if menu_options == 'main_menu':
        while(True):
            print_menu ()
    option == ''
    try:
        option =int (input('Insira uma opção'))
    except:
        print('Opcao errada, insira um numero ...')
    if option == 1:
        listdir()
    elif option == 2:
        printfile()
    elif option == 3:
     nowfile()
