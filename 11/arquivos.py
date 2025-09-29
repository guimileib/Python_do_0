'''
EX1
Crie um programa que pergunte ao usuário um item que ele deseja adicionar à sua lista de compras. 
O programa deve salvar este item em um arquivo chamado lista_compras.txt.
Dica: Use o modo 'a' (append) para que, a cada vez que você rodar o programa, um novo item seja adicionado ao final da lista, 
em vez de apagar os anteriores. 
Não se esqueça de adicionar um \n no final do item para que o próximo fique em uma nova linha.
EX2:
Agora, crie um segundo programa que leia o arquivo lista_compras.txt (criado no exercício anterior) 
e exiba cada item da lista na tela, um por linha.
'''

item = input('Adicione algum item na sua lista de compras: ')

with open('lista_compras.txt', 'a') as f:
    f.write(f'{item}\n')

with open('lista_compras.txt', 'r') as f:
    print('Sua lista de compras: ')
    cont = 0
    for item in f:
        cont = 1 + cont 
        print(f'{cont}. {item.strip()}')

