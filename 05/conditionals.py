'''
Ex1:
Escreva um programa que pergunte a idade do usuário.
Se a idade for maior ou igual a 18, exiba a mensagem: "Você é maior de idade."
Caso contrário (se for menor que 18), exiba: "Você é menor de idade."

Ex2: 
Crie um programa que peça ao usuário para inserir duas notas (de 0 a 10). O programa deve calcular a média dessas notas e exibir uma das seguintes mensagens:
Se a média for maior ou igual a 7, exiba: "Aprovado!"
Se a média for maior ou igual a 5, mas menor que 7, exiba: "Recuperação."
Se a média for menor que 5, exiba: "Reprovado."
'''

idade = int(input("Digite aqui a sua idade: "))

if idade < 18:
    print("EPA EPA EPA, Você ainda é menor de idade...\n")
elif idade >= 18:
    print('OK, tudo bem você já pode ver certas coisas...\n')

print("++++++++++++ Indo para o Exercício 2")

nota1 = float(input("Digite um valor para nota 1, de 0 a 10: "))
nota2 = float(input("Digite um valor para nota 2, de 0 a 10: "))

media = (nota1 + nota2) / 2


if media >= 7:
    print("Aprovado!")
elif media >= 5 and media < 7:
    print("Recuperação")
else: 
    print("Reprovado")




