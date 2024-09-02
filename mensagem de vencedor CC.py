#Programa de mostrar mensagem de vencedor......
# Catarina Costa 22-03-2022...........
#Indicacao das variaveis...#
qtd= 1, iten= "Tesla X", valor= 65400.54 nome= ‘Catarina"
#Indicacao da mensagem...#
txt = "Parabéns, sra. {}, acabou de ganhar {}{}  no valor de {}"
print(txt.format(nome).format(qtd).format(iten).format(valor))
