import math
import random

menu_options = {
    1: 'Factorial',
    2: 'Primos',
    3: 'Primos num intervalo',
    4: 'Sair',
    5: 'Numeros Tios',
}

def eTio(n):
    ans = False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            ans = True
    return ans

def print_menu():
    for key in menu_options.keys():
        print (key, '--', menu_options[key] )

def option1():
     n = input("Insira um numero: ")
     factorial = 1
     if int(n) >= 1:
        for i in range (1,int(n)+1):
            factorial = factorial * i
        print("Fatorial de",n , " e : ",factorial)

def option2():
     num = int(input("Insira um numero: "))
     if num > 1:
        for i in range(2,num):
            if (num % i) == 0:
                print(num,"Nao é primo")
                print(i,"vezes",num//i,"e",num)
                break
        else:
            print(num,"e um numero primo")
     else:
        print(num,"Nao e um numero primo")

def option3():
     menor = int(input("Intruduza o menor numero do intervalo: "))
     maior = int(input("introduza o maior numero no intervalo: "))
     for num in range(menor, maior+1):
         for x in range(2,num):
             if num%x==0:
                 break
         else:
             print(num)

def option5():
     print("Imprime um conjunto de numeros tios, avós, netos e a p que os P:")
     menor = random.randint(1,100)
     maior = random.randint(menor,150)
     for x in filter(eTio, range(menor, maior)):
        print(x)
        print('todos os numeros acima são tudo menos primos! Nem que seja por incesto! Obrigado Eça de Queiroz')

if __name__=='__main__':
    while(True):
        print_menu()
        option = ''
        try:
            option = int(input('Insira uma opcao: '))
        except:
            print('Opcao errada, insira um numero ...')
        if option == 1:
           option1()
        elif option == 2:
            option2()
        elif option == 3:
            option3()
        elif option == 4:
            print('Obrigado por usar uma treta de programa!')
            exit()
        elif option == 5:
            option5()
        else:
            print('Opcao errada, insira um numero entre 1 e 5')