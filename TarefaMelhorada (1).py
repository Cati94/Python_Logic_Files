# -----------------------------------------------------------------------------
# Tarefa 20/04/2022
# 20/04/2022 - 26/04/2022, Jose Abreu
# ------------------------------------------------------------------------------

from os import system
from time import sleep

# Ativar a simulação em consola para utilizar os system("cls")

def PalindromoClear():
    sleep(1.3)
    system("cls")
    print("-------------- Palíndromo --------------")


def TeclaPraContinuar():
    input("Pressione qualquer tecla para voltar ao menu...")
    system("cls")

def Numero():
    Numero = input("Introduza apenas um número inteiro e positivo: ")
    return Numero


def Palavra():
    String = input("Introduza qualquer e apenas uma palavra: ")
    return String


def SairDoMenu():
    print("A sair do menu...")


def Inválido():
    print("Opção inválida\n")


def NaoExiste():
    print("Opção não existente\n")


def Menu():
    print("""        --------- MENU ----------
        1 - Conta Vogais        |
        2 - Palíndromo/Capicuas |
        3 - Data por extensão   |
                                |
        0 - Sair                |
        -------------------------""")
    Valor = int(input("=> "))

    return Valor


def Data():
    while True:
        try:
            system("cls")
            print("------------------------- Data por extensão -------------------------")
            print("\t     (Não contamos Fevereiro como ano bissexto)")
            String = input("Introduza a sua data de nascimento no seguinte formato (dd/mm/aaaa): ")

            if (String[0] or String[1] or String[3] or String[4] or String[6] or String[7] or String[8] or String[9]).isdigit() == False:
                print("Formato de data inválido ")
                sleep(1.2)

            elif len(String) != 10:
                print("Formato de data inválido ")
                sleep(1.2)

            else:
                StringDia = int(String[0:2])
                StringMes = int(String[3:5])
                StringAno = int(String[6:10])

                # print(StringDia)
                # print(StringMes)
                # print(StringAno)

                if String[2] != "/" or String[5] != "/":
                    print("Formato de data inválido\n")
                    sleep(1.2)

                elif StringDia == 00 or StringDia < 0 or StringDia > 31:
                    print("Dia de nascimento inválido")
                    sleep(1.2)

                elif StringMes == 00 or StringMes < 0 or StringMes > 12:
                    print("Mês de nascimento inválido")
                    sleep(1.2)

                elif StringAno == 0000 or StringAno < 0 or StringAno > 2021:
                    print("Ano de nascimento inválido")
                    sleep(1.2)

                else:
                    if StringMes == 1:
                        StringMes = "Janeiro"

                    elif StringMes == 2:
                        StringMes = "Fevereiro"

                    elif StringMes == 3:
                        StringMes = "Março"

                    elif StringMes == 4:
                        StringMes = "Abril"

                    elif StringMes == 5:
                        StringMes = "Maio"

                    elif StringMes == 6:
                        StringMes = "Junho"

                    elif StringMes == 7:
                        StringMes = "Julho"

                    elif StringMes == 8:
                        StringMes = "Agosto"

                    elif StringMes == 9:
                        StringMes = "Setembro"

                    elif StringMes == 10:
                        StringMes = "Outubro"

                    elif StringMes == 11:
                        StringMes = "Novembro"

                    elif StringMes == 12:
                        StringMes = "Dezembro"

                    else:
                        print(end="")

                    if StringDia == 31 and (StringMes == "Abril" or StringMes == "Junho" or StringMes == "Setembro" or StringMes == "Novembro"):
                        print("Data inválida, {} não tem 31 dias".format(StringMes))
                        sleep(2)

                    elif (StringDia == 31 or StringDia == 30 or StringDia == 29) and StringMes == "Fevereiro":
                        print("Data inválida, {} só tem 28 dias".format(StringMes))
                        sleep(2)

                    else:
                        print("O senhor/a nasceu no dia", StringDia, "de", StringMes, "do ano de", StringAno, "\n")
                        TeclaPraContinuar()
                        break

        except ValueError:
            Inválido()


def Palindromo():
    system("cls")

    while True:
        try:

            print("""           --------- SUBMENU ------
            1 - Palindromos        |
            2 - Capicuas           |
                                   |
            0 - Voltar             |
            ------------------------""")
            Valor = int(input("=> "))

            if Valor == 0:
                SairDoMenu()
                system("cls")
                break

            elif Valor == 1:
                system("cls")
                print("-------------- Palíndromo --------------")

                String = input("Introduza qualquer e apenas uma palavra: ")

                while String.isalpha() == False:

                    if String.find(" ") != -1:
                        print("Introduziu mais de uma palavra\n")
                        PalindromoClear()
                        String = Palavra()

                    else:
                        print("Introduza apenas palavras")
                        PalindromoClear()
                        String = Palavra()

                while String.isalpha() == True:

                    while len(String) == 1 or len(String) == 0:
                        if len(String) == 1:
                            print("Apenas um carater não forma uma palavra\n")
                            sleep(1.4)
                            system("cls")
                            print("-------------- Palíndromo --------------")
                            String = Palavra()

                        elif len(String) == 0:
                            print("Nao foi introduzido nada\n")
                            PalindromoClear()
                            String = Palavra()

                        else:
                            print(end="")

                    while String.find(" ") != -1:
                        print("Introduziu mais de uma palavra\n")
                        PalindromoClear()
                        String = Palavra()

                        if len(String) == 1:
                            print("Apenas um carater não forma uma palavra\n")
                            sleep(1.4)
                            system("cls")
                            print("-------------- Palíndromo --------------")
                            String = Palavra()

                        elif len(String) == 0:
                            print("Nao foi introduzido nada\n")
                            PalindromoClear()
                            String = Palavra()

                        else:
                            print(end="")

                    break

                StringCopia = String
                String = String[::-1]
                StringInversa = String

                if StringInversa == StringCopia:

                    print("É um palíndromo\n")
                    TeclaPraContinuar()
                    break

                else:
                    print("Não é um palíndromo\n")
                    TeclaPraContinuar()
                    break

            elif Valor == 2:
                system("cls")
                print("-------------- Capicua --------------")

                String = Numero()

                while String.isdecimal() == False:

                    if String.find(" ") != -1:
                        print("Introduziu mais de um número\n")
                        PalindromoClear()
                        String = Numero()

                    else:
                        print("Introduza apenas um número inteiro e positivo")
                        sleep(1.5)
                        system("cls")
                        print("-------------- Capicua --------------")

                        String = Numero()

                StringCopia = String
                String = String[::-1]
                StringInversa = String

                if StringInversa == StringCopia:
                    print("O número introduzido é uma capicua\n")
                    TeclaPraContinuar()
                    break

                else:
                    print("O número introduzido não é uma capicua\n")
                    TeclaPraContinuar()
                    break

            else:
                NaoExiste()
                TeclaPraContinuar()

        except ValueError:
            Inválido()
            TeclaPraContinuar()


def ContaVogais():
    system("cls")

    print("\n------- Conta vogais -------")

    print("Introduza qualquer palavra")
    print("(Minúscula ou Maiúscula)")
    String = input("=> ")

    while String.isalpha() == False:
        print("\nApenas são permitidas letras")
        sleep(1.3)
        system("cls")

        print("\n------- Conta vogais -------")

        print("Introduza qualquer palavra")
        print("(Minúscula ou Maiúscula)")
        String = input("=> ")

    cont = 0
    ListaVogais = []

    for n in range(len(String)):
        if String[n] == "a" or String[n] == "e" or String[n] == "i" or String[n] == "o" or String[n] == "u"\
                or String[n] == "A" or String[n] == "E" or String[n] == "I" or String[n] == "O" or String[n] == "U":

            cont += 1
        else:
            cont = cont

    StringVogais = String

    for n in range(len(String)):
        if String[n] == "a" or String[n] == "A":
            ListaVogais.append(String[n].upper())

        elif String[n] == "e" or String[n] == "E":
            ListaVogais.append(String[n].upper())

        elif String[n] == "i" or String[n] == "I":
            ListaVogais.append(String[n].upper())

        elif String[n] == "o" or String[n] == "O":
            ListaVogais.append(String[n].upper())

        elif String[n] == "u" or String[n] == "U":
            ListaVogais.append(String[n].upper())

        else:
            ListaVogais.append("")

    print("\nAs vogais da palavra =>", ListaVogais)
    print()

    if cont == 0:
        print("Não existem vogais na palavra introduzida\n")

    elif cont == 1:
        print("Esta palavra tem apenas uma vogal\n")

    else:
        print("Esta palavra tem", cont, "vogais\n")

    TeclaPraContinuar()


    # -------------------------------- Codigo Principal --------------------------------

while True:
    try:
        Valor = Menu()

        if Valor == 0:
            SairDoMenu()
            break

        elif Valor == 1:

            ContaVogais()

        elif Valor == 2:

            Palindromo()

        elif Valor == 3:

            Data()

        else:
            NaoExiste()
            TeclaPraContinuar()

    except ValueError:
        Inválido()
        TeclaPraContinuar()
