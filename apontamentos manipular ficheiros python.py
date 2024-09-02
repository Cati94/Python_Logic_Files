# ------------------- Apontamentos de como manipular ficheiros ---------------------
# ------------------ Catarina Costa 5-5-2022 ---------------------------------------
# ----------------------------------------------------------------------------------
#Programa que dado um diretório mostra a listagem dos ficheiros existentes, depois consoante a escolha do utilizador mostra os ficheiros de uma determinada extensão ou apenas as pastas.
# Pede qual o ficheiro txt quer visualizar, indicando quando se encontra aberto para as operações e depois quando fica fechado. # 
# Deve indicar também qual o seu modo e o nome. # 


import os
# Comando para eleger a directory #
path = input('What is the directory: ')
# Comando para mudar de directory #
os.chdir('C:/Users/pmato/Desktop/CET 3')
# Mostra directory current working #
print('Diretorio onde estamos a trabalhar: ', os.getcwd()) 

# Comando que devolve uma lista de ficheiros existentes # 
ficheiros = os.listdir()
print(ficheiros)

# seleciona ficheiros de determinada extensao#
ext = input('Qual a extensao: ')
ext_total = '.' + ext
for f in ficheiros:
    if f.endswith(ext_total): 
     print(f)

 # Seleciona apenas os ficheiros # 
for f in ficheiros:
        if os.path.isfile(f):
         print(f)

# Duas formas de selecionar apenas as pastas #
for f in ficheiros:
    # is not os.path.isfile(f): 
    if os.path.isdir(f): 
        print(f)

# ------------------------------------------------------------------------------------------------------------------------------------# 

# Mostrar lista de pastas existentes #
print(os.listdir())
print('\n As pastas existentes sao:\n')

# Visualizar ficheiros so destas extensoes#
ext = ['.docx', '.pdf'] 

# lista extensoes para mostrar ficheiros #
for f in os.listdir():
    #for n in ext:
        #if f.endswith(n):
            #print(f)

    for f in os.listdir():
        if os.path.isdir(f):
            print(f)

# Identificar e remover pasta se existir #
    if os.path.exists('Música'):
        os.rmdir('Música')
    print('\nA pasta foi removida')
else:
    print('\nA pasta não existe.') 


# Criar pasta no diretório e mostrar # 
os.mkdir('Música')
print('\n\n')

for f in os.listdir():
    if os.path.isdir(f):
        print(f) 

# -------------------------------------------------------------------------------------------------------------------------------- #

# Abrir o ficheiro em modo leitura #
print('\n1ª forma de leitura de um ficheiro\n\n')
f = open('Teste1.txt', 'r') # abertura de um ficheiro em modo de leitura
print(f.read())
f.close()

print('\n2ª forma de leitura de um ficheiro\n\n')

try:
    nome = input('Qual o ficheiro que pretende abrir:')
    nome += '.txt'
    f = open(nome, 'r')  # abertura de um ficheiro em modo de leitura
    print(f.read())
except FileNotFoundError:
    print('O ficheiro não existe')
    print('Tente outra vez.')
finally:
    if f.close() == None:
        print('entrou')
        f.close()

print('\n3ª forma de leitura de um ficheiro\n\n')

with open('Teste1.txt', 'r') as f:
    print(f.read())

with open('Teste.txt', 'r') as f:
    # texto = f.read() # este método devolve uma string
    texto = f.readline(12)
    print(type(texto))
    print(texto)

print('\n-------------------------------------------------------------\n')

with open('Teste.txt', 'r') as f:
    aux = 0;
    while True:
        aux += 1
        linha = f.readline()
        if not linha:
            break
        print(linha, end='')
    print('\n', type(linha), 'números: ', aux)

print('\n-------------------------------------------------------------\n')

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

# ---------------------------------------------------------------------------------------------- #
os.chdir('C:/Users/pmato/Desktop/CET 3')

l_ext = []

print('Ficheiros existentes no diretório:\n')

for file in os.listdir():
    print(file)
    nome, ext = os.path.splitext(file)
    if ext != '':
        l_ext.append(ext)

l_aux = []

for n in l_ext:
    if n not in l_aux:
        l_aux.append(n)
print('\nTipos de extensões existentes no diretório: ', l_aux)

while True:
    try:
        ext = ''
        print(l_aux)
        while ext not in l_aux or nome not in os.listdir():
            nome = input('Qual o ficheiro que pretende abrir: ')
            l = nome.split('.')
            ext = l[len(l) - 1]
            ext = '.' + ext
            if ext not in l_aux:
                print('Ficheiro não existente. Nome ou extensão de ficheiro errado, volte a tentar.')

        with open(nome, 'r') as f:
            print(f.read())
        break
    except ValueError:
        print('erro')
# ------------------------------------------------------------------------------------------------------ #
# with open('Teste1.txt', 'r', encoding='utf-8') as f: # o argumento encoding muda a codificação da escrita no ficheiro
    # print('Conteúdo do ficheiro inicial:\n')
    # print(f.read())

texto = ('Bom dia CET3\n'
         'Hoje é sexta-feira...\n'
         'e vamos ver como escrever num ficheiro txt.\n')

with open('Teste1.txt', 'w', encoding='utf-8') as f: # o modo "W" limpa o conteudo do ficheiro e escreve o novo conteúdo
    f.write(texto)

with open('Teste1.txt', 'r', encoding='utf-8') as f:
    print('\nNovo conteúdo do ficheiro:\n')
    print(f.read())

new_text = input('Escreva o novo texto para acrescentar no ficheiro: ')

with open('Teste1.txt', 'a', encoding='utf-8') as f: # o modo "a" limpa o conteudo do ficheiro e escreve o novo conteúdo
    f.write(new_text)

with open('Teste1.txt', 'r', encoding='utf-8') as f:
    print('\nNovo conteúdo do ficheiro:\n')
    print(f.read())
# --------------------------------------------------------------------------------------------------------------------------- #

with open('Teste1.txt', 'w', encoding='utf-8') as f:
    print('Escreva a informação que pretende gravar no ficheiro (0 para terminar):\n')
    while True:
        linha = input('=> ')
        if linha == '0':
            break
        linha += '\n'
        f.write(linha)

with open('Teste1.txt', 'r', encoding='utf-8') as f:
    print(f.read())


with open('Teste2.txt', 'w', encoding='utf-8') as f:
    texto = ['12312\n', 'hvqjhfgv whfgqrigf hgflqirg ugf \n', '314gqfkó ó\n']

    f.writelines(texto)

with open('Teste2.txt', 'r', encoding='utf-8') as f:
    print(f.read())