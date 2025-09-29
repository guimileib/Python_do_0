'''
EX1:
Pegue o exercício da "Calculadora de Dobro" (Dia 4). Modifique-o para que ele use um bloco try...except.
 Se o usuário digitar algo que não possa ser convertido para um número inteiro, o programa deve exibir a mensagem "Entrada inválida. 
 Por favor, digite um número." sem quebrar.
'''

print('=== Calcular o dobro: ===')
result = True
while result == True:
    try: 
        nmr = input("Digite algum número: ")
        nmr_convertido = int(nmr)
        nmr_dobro = nmr_convertido * 2
        print(f"O dobro do número que você digitou é: {nmr_dobro}")
        result = False
    except:
        print('Entrada inválida. Por favor, digite um número.')
        result = True


'''
EX2:
Crie um programa que peça ao usuário dois números. O programa deve tentar dividir o primeiro pelo segundo e exibir o resultado.
O programa precisa ser seguro contra dois tipos de erro:

O usuário digita um texto em vez de um número (ValueError).

O usuário digita 0 como o segundo número, o que causa um erro de divisão por zero (ZeroDivisionError).

Use try e múltiplos except para capturar cada erro e dar uma mensagem específica para cada um.
'''



def calc():
    try: 
        n1 = float(input("Digite um número: "))
        n2 = float(input("Digite um número: "))
        div = (n1/n2)
        return div
    except ValueError:
        return 'Digite um valor válido para realizar a divisão!'
    except ZeroDivisionError:
        return 'Não é possível realizar uma divisão por 0'

result = calc()
print(result)