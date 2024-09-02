from importlib.metadata import files
import os 
pasta = input ('Qual o caminho: ')
os.cmdir ("c:\Users\Pokédex\desktop\UX/UI") # change diretory
print ('diretorio onde estamos a trabalhar:', os.getcwd()) # show diretory now
ficheiros = os.listdir() # devolve os ficheiros existentes em lista
print (ficheiros)
ext = input ('Qual a extensao:' )
ext_total = '.' + ext
    for f in ficheiros: 
        if  f.endswith(ext_total) :  # seleciona os ficheiros de determinada extensao
    #  print(f)


    for f in ficheiros:
        if os.path.isfile (f): # seleciona apenas os ficheiros
     print(f)
for f in ficheiros:


is not os.path.isfile (f): #seleciona apenas pastas #
