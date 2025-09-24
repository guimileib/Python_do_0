"""
EX1:
Escreva um programa que use um laço while para fazer uma contagem regressiva de 10 até 1. Ao final, depois do laço, exiba a mensagem "Fogo!".

EX2:
Crie um programa que peça ao usuário para digitar uma senha. O programa deve continuar pedindo a senha enquanto o que o usuário digitar for diferente 
da senha correta (que você pode definir como "1234"). Quando o usuário acertar a senha, o programa deve exibir "Acesso concedido." e terminar.
"""
'''
contador = 1

while contador <= 10:
    print(contador)
    contador = contador + 1

print("Fogo!")'''

senha_correta = 1234
senha = int(input("Digite sua senha por gentileza: "))

while senha != senha_correta:
    senha = int(input("Digite sua senha por gentileza: "))

print("Acesso concedido")