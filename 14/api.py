'''
Exercício 1: Consultor de Endereço por CEP
Vamos usar a API gratuita "ViaCEP" para buscar um endereço a partir de um CEP brasileiro.
Crie um programa que:
Peça ao usuário para digitar um CEP (apenas os números).
Use o requests para fazer uma chamada à API: https://viacep.com.br/ws/SEU_CEP_AQUI/json/
Exiba o logradouro, bairro, cidade e estado correspondentes àquele CEP.
'''
import requests 

cep = input('Digite seu CEP para consulta (apenas números): ')
url = f'https://viacep.com.br/ws/{cep}/json/'

try:
        
    response = requests.get(url)

    if response.status_code == 200:
        dados_endereco =  response.json()

        if 'erro' in dados_endereco:
            print("CEP não encontrado ou inválido")
        else:
            print('\n== Enderço encontrado: ==')
            print(f'Logradouro: {dados_endereco['logradouro']}')
            print(f'Bairro: {dados_endereco['bairro']}')
            print(f'Cidade:{dados_endereco['localidade']}')
            print(f'Estado: {dados_endereco['uf']}')
    else:
        print(f'Erro na requisição. Código: {response.status_code}')

except requests.exceptions.RequestException as e:
    print(f'Erro de conexão: {e}')