'''
Exercício: Calculadora Simples com Tratamento de Erros - Revisão Dia 1 ao 19.
O seu objetivo é criar uma calculadora que roda no terminal, mas de forma segura e organizada.
Crie uma função chamada calcular(n1, n2, operacao) que recebe dois números e uma string de operação ("soma", "sub", "mult", "div").
Dentro da função, use if/elif/else para realizar a operação correta e retornar o resultado.
Ainda dentro da função, use um bloco try/except para lidar especificamente com o erro ZeroDivisionError. Se a divisão por zero ocorrer, a função deve retornar a string "Erro: Divisão por zero".
No seu código principal (fora da função), peça ao usuário para digitar o primeiro número, o segundo número e a operação.
Envolva o input dos números em um bloco try/except para capturar ValueError (caso o usuário digite um texto em vez de um número). Se isso acontecer, exiba "Entrada inválida."
Se a entrada for válida, chame sua função calcular e imprima o resultado.
'''

def main(): 
    while True:    
        try:
            n1 = int(input("Digite um valor para n1: "))
            n2 = int(input("Digite um valor para n2: "))
            print(f"Valores digitados: n1: {n1} e n2: {n2}")
            r = input("Deseja alterar os valores? [y/n] ")
            if r == "n":
                pass
            else:
                n1 = int(input("Digite um valor para n1: "))
                n2 = int(input("Digite um valor para n2: "))
                print(f"Valores digitados: n1: {n1} e n2: {n2}")
            print("======= Operações matemáticas: =======\n")
            
            op = input("Qual tipo de operação você deseja realizar? ").lower().strip()
            if op == '':
                return "Digite uma operação válida"
            resultado = calcular(n1, n2, op)
            if resultado is not None:
                print(f"Resultado da operação {op}: {resultado}\n")
                resp = input("Deseja realizar mais operações? [y/n] ")
                if resp == "n":
                    print("Saindo...")
                    raise KeyboardInterrupt

        except ValueError:
            print("Digite um valor válido!\n")
        except KeyboardInterrupt:
            print("Programa interrompido pelo usuário")
            break

def calcular(n1, n2, operacao):
    print(f"Operação escolhida {operacao}")
    try:
        if "soma" in operacao:
            return n1 + n2
        elif "sub" in operacao:
            sub = n1 - n2
            return sub
        elif "mult" in operacao:
            mult = n1 * n2 
            return mult
        elif "div" in operacao:
            div = n1 / n2
            return div
        else:
            print("Tipo de operação escolhido inválido")
            return None
    except ZeroDivisionError:
        print("Não é possível dividir nenhum número por zero.")
        return None

if __name__ == "__main__":
    main()
    