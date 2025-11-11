'''
Exercício 2:
Vamos criar um programa que gerencia um inventário de loja, salvando os dados em um arquivo.

1. Importe o módulo json.

2. Crie um while True loop que funciona como um menu principal. Ele deve perguntar ao usuário: "O que deseja fazer? (1-Adicionar item, 2-Listar itens, 3-Sair)".

3. Se "1-Adicionar":

- Peça ao usuário o nome do item e a quantidade.
- Crie um dicionário para o item: item = {'nome': nome_item, 'quantidade': int(quantidade_item)}.
- Abra o arquivo inventario.txt em modo de append ('a').
- Use json.dumps(item) para converter o dicionário em uma string JSON e a escreva no arquivo, seguida de uma quebra de linha (\n).

4. Se "2-Listar":

- Use try/except FileNotFoundError para o caso do arquivo ainda não existir.
- Abra inventario.txt em modo de leitura ('r').
- Use um laço for para ler cada linha do arquivo.
- Para cada linha, use json.loads(linha) para converter a string JSON de volta em um dicionário.
- Imprima os dados do dicionário de forma formatada (ex: f"- Item: {item['nome']}, Quantidade: {item['quantidade']}").

5. Se "3-Sair": Use break para sair do loop while.
'''

import json


def adicionar():
    nome_item = input("Digite o nome do item:")
    qnt_item = input("Digite a quantidade:")
    item = {'nome': nome_item, 'quantidade': int(qnt_item)}

def listar():
    try:
        pass
    except FileNotFoundError:
        return "Lista não encontrada"

def process_request(request):
    match request:
        case 1:
            adicionar()
        case 2:
            listar()
        case _:
            return "Saindo do programa"

def main():
    while True:
        try:
            print("1. Adicionar")
            print("2. Listar")
            print("3. Sair")

            user = input("O que deseja fazer?")
            process_request(user)
            if(user == "3"):
                break
        except ValueError:
            print("Digite um valor válido")
        except KeyboardInterrupt:
            print("Programa interrompido pelo usuário")
            break



