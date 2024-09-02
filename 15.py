# -------------------------------------------------------------------------------------------
# Manipulação de ficheiros
# 03-05-2022, Paulo Rodrigues
# -------------------------------------------------------------------------------------------

import os

os.chdir('C:/Users/pmato/Desktop/CET 3')
print('\n\nO diretório onde nos encontramos: ', os.getcwd())

# print(os.listdir())

print('\nAs pastas existentes são:\n')

# for f in os.listdir():
    # if f.endswith('.txt') or f.endswith('docx'):
        # print(f)

# ext = ['.docx', '.pdf'] # extensões para se visualizar os ficheiros pretendidos

# bloco de código que utiliza a lista de extensões para mostrar os ficheiros
#for f in os.listdir():
    #for n in ext:
        #if f.endswith(n):
            #print(f)

for f in os.listdir():
    if os.path.isdir(f):
        print(f)

if os.path.exists('Música'):
    os.rmdir('Música')
    print('\nA pasta foi removida')
else:
    print('\nA pasta não existe.')

os.mkdir('Música')

print('\n\n')

for f in os.listdir():
    if os.path.isdir(f):
        print(f)