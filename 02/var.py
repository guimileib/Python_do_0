# str - texto, sempre em aspas
#int - integer -  números inteiros
# float - numeros com casas decimais - 1.75, 9.5
# bool - 0 ou 1 - true ou false

'''
Crie variáveis para armazenar seu nome (texto), sua idade (número inteiro), 
sua altura em metros (número decimal) e se você é estudante (booleano). 
Em seguida, use print() para exibir o valor de cada uma dessas variáveis
'''

nome = str(input('Qual o seu nome? '))
idade = int(input('Qual sua idade? '))
altura = float(input('Qual sua altura (em metros): '))

estudante = bool(int(input('Você é estudante? (1 para sim, 0 para não): ')))
'''
resposta_estudante = input('Você é estudante? (sim/não ou s/n): ').lower()
estudante = resposta_estudante in ['sim', 's', 'true', '1']
'''


dict = [nome, idade, altura, estudante]
for x in dict:
    print(x)