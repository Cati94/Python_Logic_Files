

# Palindromo - Parte do codigo para opcao 2 - diz se a palavra é Palindromo ou nao # 
word = input("Write a word: ")
if str(word) == str(word)[::-1] :
        print("Palindrome")
else:
        print("Not Palindrome")
