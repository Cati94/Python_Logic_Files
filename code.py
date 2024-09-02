# ------------------------------------------------------------------------ #
# ----------Programa de manipulacao de ficheiros em python --------------- #
# ----------Catarina Correia da Costa ------------------------------------ #
# ---------- 11 de maio de 2022 ------------------------------------------ #

import os

# Comando para mudar a directoria e mostrar onde trabalho #
path = input('What is the directory: ')
os.chdir('C:\Users\Pokédex\Desktop\javou')
print('show me the current directory: ', os.getcwd()) 

# Listar ficheiros existentes # 
ficheiros = os.listdir()
print(ficheiros)

# Identificar pasta e eliminar # 
if os.path.exists('files'):
        os.rmdir('files')
print('\n A pasta foi removida')
else:
print('\n A pasta não existe')


# Criar pasta no diretório e mostrar # 
os.mkdir('files')
print('\n\n')

for f in os.listdir(): 
    if os.path.isdir(f):
        print(f) 

# Abrir ficheiro em modo leitura e escrita#
with open('Teste.txt', 'a+') as f:
    texto = f.readlines()
    info = '\n\nO ficheiro ' + f.name + ' está '

    print('O conteúdo do ficheiro é:\n')
    for l in texto:
        print(l, end='')
    # f.name devolve o nome do ficheiro e f.closed devolve um boolean, True ou False, caso esteja aberto ou fechado
    print('\n\nO ficheiro ' + f.name + ' está ' + ('fechado' if f.closed else 'aberto'))
    if f.mode == 'r':
        print('O modo é de leitura')
    elif f.mode == 'a+':
        print('O modo é de leitura/escrita')
if f.closed:
    info += 'fechado'
else:
    info += 'Aberto'
print(info)

