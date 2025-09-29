'''
EX1:
Crie uma função chamada saudar() que não recebe parâmetros e apenas exibe a mensagem "Bem-vindo(a) ao meu programa!". 
Em seguida, chame essa função duas vezes no seu código.
'''

def saudar():
    print("Bem vindo(a) ao meu programa")

saudar()
saudar()

'''
EX2:
Crie uma função chamada calcular_area_retangulo() que recebe dois parâmetros, largura e altura. 
A função deve calcular a área do retângulo (largura * altura) e retornar o valor. 
No seu código principal, chame a função com valores de sua escolha e exiba o resultado retornado.
'''

def calcular_area_retangulo(l, h):
    area = (l * h)
    return area


print('==== Calculo da área do retângulo =====')
largura = float(input('Digite a largura do seu retângulo: '))
altura = float(input('Digite a altura do retângulo: '))

result = calcular_area_retangulo(largura, altura)
print(result)
