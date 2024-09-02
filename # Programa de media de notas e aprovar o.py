# Programa de media de notas e aprovar ou reprovar alunos # 
# Catarina Costa 24-7-2024 # 
# Introdução das variaveis # 
a = int(input("digite a nota do primeiro bimestre"))
b = int (input("digite a nota do segundo bimestre"))
c = int(input("digite a nota do terceiro bimestre"))
# Calcular a media #
media = (a+b+c)/3
# Condições de aprovado ou reprovado - if else elif # 
if (media >= 7):
    print("aprovado")
elif(media>=5 and media<=7):
    print("recuperacao")
if (media <5):
    print ("reprovado")