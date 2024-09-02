# -------------------------------------------------------------------------------------------
# Manipulação de ficheiros
# 29-04-2022, Paulo Rodrigues
# -------------------------------------------------------------------------------------------

import os

# path = input('Qual o caminho: ')

os.chdir('C:/Users/pmato/Desktop/CET 3') # muda o diretório de onde estamos a trabalhar, "change directory"
# print('Diretorio onde estamos a trabalhar: ', os.getcwd()) # mostra o diretorio atual, ou seja, onde estamos a trabalhar

ficheiros = os.listdir() # este método devolve os ficheiros exisytentes num diretorio dentro de uma lista

# print(ficheiros)

# ext = input('Qual a extensão: ')

# ext_total = '.' + ext

# for f in ficheiros:
    # if f.endswith(ext_total): # seleciona apenas os ficheiros com uma determinada extensão
        # print(f)

# for f in ficheiros:
    # if os.path.isfile(f): # seleciona apenas os ficheiros
        # print(f)

for f in ficheiros:
    # is not os.path.isfile(f): # seleciona apenas as pastas
    if os.path.isdir(f): # seleciona apenas as pastas
        print(f)