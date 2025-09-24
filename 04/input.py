'''
Ex1
Escreva um programa que pergunte o nome do usuário e a cidade onde ele mora. Em seguida, exiba uma mensagem de boas-vindas usando f-string, como: 
"Olá, [nome]! Que legal que você é de [cidade]."

Ex2:
Escreva um programa que peça ao usuário para digitar um número. 
Em seguida, o programa deve converter esse número para inteiro, calcular o dobro e exibir o resultado em uma frase formatada. Ex: "O dobro de 5 é 10."

'''

#Ex1:

nome = input("Qual o seu nome? ")
cidade = input("Qual a cidade que você mora? ")

print(f"Olá, {nome} bom saber que você mora em {cidade} rs rs..")

print("EXERCÍCIO 2 ...\n")
#Ex2:

nmr = input("Digite algum número: ")

nmr_convertido = int(nmr)

nmr_dobro = nmr_convertido * 2

print(f"O dobro do número que você digitou é: {nmr_dobro}")

