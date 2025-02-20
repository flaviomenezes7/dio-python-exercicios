################ OPERAÇÕES MATEMÁTICAS ################

def calculadora():
    num1 = float(input("Digite o primeiro número: ")) # Declarando uma variavel do tipo float e recebendo um valor do tipo float
    num2 = float(input("Digite o segundo número: "))
    
    print(f"Soma: {num1 + num2}") # Imprimindo o resultado da soma dos dois números
    print(f"Subtração: {num1 - num2}") # Imprimindo o resultado da subtração dos dois números
    print(f"Multiplicação: {num1 * num2}") # Imprimindo o resultado da multiplicação dos dois números
    print(f"Divisão: {num1 / num2}" if num2 != 0 else "Não é possível dividir por zero") # Imprimindo o resultado da divisão dos dois números, caso o segundo número seja diferente de zero, senão imprime a mensagem "Não é possível dividir por zero"

def verificar_par_ou_impar():
    num = int(input("Digite um número: ")) # Declarando uma variavel do tipo int e recebendo um valor do tipo int
    print("Par" if num % 2 == 0 else "Ímpar") # exibindo o "par" se o resto da divisão do número por 2 for igual a zero, senão exibe "ímpar"

def tabuada():
    num = int(input("Digite um número: "))
    for i in range(1, 11): # o for irá percorrer de 1 a 10
        print(f"{num} x {i} = {num * i}") # Imprimindo a tabuada

################ MANIPULAÇÃO DE STRINGS ################

def contador_vogais():
    palavra = input("Digite uma palavra:")
    vogais = "aeiou" # Declarando uma variavel com as vogais
    contador = 0
    for letra in palavra: # o for irá percorrer cada letra da palavra digitada pelo usuário
        if letra in vogais:
            contador += 1
    print(f"A palavra {palavra} tem {contador} vogais")

def contador_de_letras(): 
    palavra = input("Digite uma palavra:") 
    print(f"A palavra {palavra} tem {len(palavra)} letras")

def validar_senha():
    import re # Importando a biblioteca re para usar expressões regulares
    
    senha = input("Digite sua senha: ")
    
    if len(senha) < 8: # Se a senha tiver menos de 8 caracteres, retorna a mensagem
        return "Senha muito curta. Mínimo 8 caracteres."
        
    if not re.search("[A-Z]", senha): # re.serach é uma função que procura por um padrão em uma string
        return "Senha deve conter pelo menos uma letra maiúscula."
        
    if not re.search("[a-z]", senha): 
        return "Senha deve conter pelo menos uma letra minúscula."
        
    if not re.search("[0-9]", senha):
        return "Senha deve conter pelo menos um número."
        
    if not re.search("[!@#$%^&*(),.?\":{}|<>]", senha):
        return "Senha deve conter pelo menos um caractere especial."
        
    return "Senha válida!"

################ CONVERSORES ################

def conversor_temperatura():
    celsius = float(input("Digite a temperatura em Celsius: ")) # Declarando uma variavel do tipo float e recebendo um valor do tipo float
    fahrenheit = (celsius * 9/5) + 32 # Declarando uma variavel e realizando a conversão de celsius para fahrenheit
    print(f"A temperatura em Fahrenheit é: {fahrenheit}") # Imprimindo a temperatura em fahrenheit

################ JOGOS ################

import random

def jogo_forca():
    palavras = ["python", "programacao", "desenvolvimento", "computador", "tecnologia"] # Lista de palavras
    palavra = random.choice(palavras) # Escolhendo uma palavra aleatória
    letras_descobertas = ["_" for _ in palavra] # Substituindo as letras da palavra por "_"
    tentativas = 6 # Número de tentativas
    letras_tentadas = set() # Conjunto de letras tentadas
    
    while tentativas > 0 and "_" in letras_descobertas: # Enquanto o número de tentativas for maior que zero e "_" estiver na lista de letras descobertas
        print("\nPalavra:", " ".join(letras_descobertas)) # Imprimindo a palavra com as letras descobertas
        print(f"Tentativas restantes: {tentativas}") # exibindo o número de tentativas restantes
        print("Letras tentadas:", ", ".join(sorted(letras_tentadas))) # exibindo as letras tentadas
        
        letra = input("\nDigite uma letra: ").lower() # Recebendo uma letra do usuário e convertendo para minúsculo
        
        if letra in letras_tentadas: # Se a letra escolhida pelo usuário estiver no conjunto de letras tentadas, exibe a mensagem
            print("Você já tentou essa letra!")
            continue
            
        letras_tentadas.add(letra) # Adicionando a letra ao conjunto de letras tentadas
        
        if letra in palavra: # se a letra estiver contida na palavra
            for i, char in enumerate(palavra): # o enumerate irá retornar o índice e o caractere da palavra. o for irá percorrer a palavra
                if char == letra: # se o caractere for igual a letra
                    letras_descobertas[i] = letra # a letra descoberta será igual a letra
            print("Letra correta!") # exibe a mensagem
        else:
            tentativas -= 1 # decrementa o número de tentativas
            print("Letra incorreta!")
    
    if "_" not in letras_descobertas: # se "_" não estiver na lista de letras descobertas
        print(f"\nParabéns! Você venceu! A palavra era: {palavra}") # exibe a mensagem
    else:
        print(f"\nGame Over! A palavra era: {palavra}")

################ CONCEITOS DE PROGRAMAÇÃO ################

def continue_break():

    for numero in range(100): # o for irá percorrer de 0 a 99
        if numero % 2 == 0: # se o número for par 
            continue # pula para a próxima iteração
        print(numero) # imprime o número
        if numero == 53: # se o número for igual a 53
            break # interrompe o loop

def gerador_fibonacci():
    def fib(): 
        a, b = 0, 1 # Declarando as variáveis a e b com os valores 0 e 1
        while True: # loop infinito
            yield a # o yield serve para retornar um valor e pausar a execução da função
            a, b = b, a + b # a variável a recebe o valor de b e a variável b recebe a soma de a e b
    
    n = int(input("Quantos números da sequência você quer gerar? "))
    generator = fib() # chamando a função fib
    for _ in range(n): # o for irá percorrer de 0 a n
        print(next(generator)) # o next serve para chamar o próximo valor do gerador

################ MENU PRINCIPAL ################

def menu():
    while True:
        print("\n=== MENU DE EXERCÍCIOS ===")
        print("1. Calculadora")
        print("2. Verificar Par ou Ímpar")
        print("3. Conversor de Temperatura")
        print("4. Contador de Vogais")
        print("5. Contador de Letras")
        print("6. Validar Senha")
        print("7. Tabuada")
        print("8. Jogo da Forca")
        print("9. Continue Break")
        print("10. Gerador de Fibonacci")
        print("0. Sair")
        
        opcao = input("\nEscolha uma opção (0-9): ")
        
        if opcao == "0":
            print("Programa encerrado!")
            break
        elif opcao == "1":
            calculadora()
        elif opcao == "2":
            verificar_par_ou_impar()
        elif opcao == "3":
            conversor_temperatura()
        elif opcao == "4":
            contador_vogais()
        elif opcao == "5":
            contador_de_letras()
        elif opcao == "6":
            print(validar_senha())
        elif opcao == "7":
            tabuada()
        elif opcao == "8":
            jogo_forca()
        elif opcao == "9":
            continue_break()
        elif opcao == "10":
            gerador_fibonacci()
        else:
            print("Opção inválida! Tente novamente.")
        
        input("\nPressione ENTER para continuar...")

################ EXECUÇÃO PRINCIPAL ################

if __name__ == "__main__":
    menu()