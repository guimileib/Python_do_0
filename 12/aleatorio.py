import random # standard list

'''
EX1:
Crie um programa que "pensa" em um número inteiro entre 1 e 10. Em seguida, peça para o usuário adivinhar qual é esse número.
 O programa deve dizer se o usuário acertou ou errou. (Por enquanto, não precisa fazer um loop, apenas uma tentativa é suficiente).
'''
v = True

while v == True:
    try:
        numero_pensado = random.randint(1,10)
        adivinha = int(input("Tente adivinhar o número de 1 a 10 que estou pensando, tentai ai vai kkkkkkk: "))
        if adivinha >= 10 or adivinha >=1:
            if adivinha == numero_pensado:
                print(f"Você acertou eu pensei no número {numero_pensado}")
                v = False
            else:
                print(f"Você errou eu não pensei no número {adivinha}")
                print(f"Eu pensei no núumero {numero_pensado}")
                tentativa = int(input("Quer tentar denovo? \n 1(sim)/ 0(não) "))
                if tentativa == 1:
                    v = True
                elif tentativa == 0:
                    v = False
                else:
                    print("Digitou errado perdeu a chance KKKKKKKKKKKKKK")
                    print("Otário!")
                    v = False
        else:
            print("Você deve digitar um número de 1 a 10, você não sabe ler?")
            v = True
    except ValueError:
        print("Digite um valor válido")
        v = True