# Programa que deteta a palavra alvo no texto#
# Catarina Costa#
frase = "Nesta frase tem a palavra alvo""O sucesso nasce do querer, da determinação, e presistência em chegar a um objetivo""Mesmo não atingindo o alvo, quem busca e vence obstáculos, no mínimo fará coisas imagináveis"
palavra = "alvo"
if palavra not in frase:
    print("A frase nao tem " + palavra)
else:
    print("A frase tem " + palavra)