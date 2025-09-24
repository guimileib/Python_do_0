"""
[Operadores Básicos:]

Soma: +

Subtração: -

Multiplicação: *

Divisão: /

Potência: ** (ex: 2**3 é 2 elevado a 3)

Módulo (resto da divisão): % (ex: 10 % 3 retorna 1)
"""

"""
Crie duas variáveis com números. Exiba na tela o resultado da soma, subtração, multiplicação e divisão dessas duas variáveis. 
Para cada operação, exiba uma frase descritiva, por exemplo: "A soma é: [resultado]"
"""

"""
Crie uma variável com um número inteiro qualquer. Use o operador de módulo (%) para descobrir se o número é par ou ímpar. 
A dica é: um número par dividido por 2 sempre tem resto 0. Exiba o resto da divisão do seu número por 2.
"""

numero1 = 10
numero2 = 11

print(f"Calculo com seu número1: {numero1} e seu número2 {numero2}")

soma = numero1 + numero2
subtracao = numero1 - numero2
multiplicacao = numero1 * numero2
divisao = numero1 / numero2

dict = [soma, subtracao, multiplicacao, divisao]
print("Resultado Exercício 1:\n")

print("O resultado da soma é ", soma)
print(f"O resultado da subtração é {subtracao}")
print(f"O resultado da multiplicaçãop é {multiplicacao}")
print(f"O resultado da divisão é {divisao}\n")

print("Exercício 2:\n")

numero3 = int(input("Digite um número inteiro para descobrir se ele é ímpar ou par: "))
# usando operador de modulo '%', para descobrir se é impar ou par:
result = numero3 % 2

if result == 0:
    print("O número digitado é par")
else:
    print("O número digitado é impar")
