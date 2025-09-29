'''
Exercício 2: Cotação do Dólar
Vamos usar outra API simples, a "AwesomeAPI", para ver a cotação do Dólar em tempo real.
Crie um programa que:
Use o requests para buscar os dados na URL: https://economia.awesomeapi.com.br/last/USD-BRL
A partir da resposta, acesse e exiba o valor de compra (bid) do Dólar em Reais.
'''
import requests

url = 'https://economia.awesomeapi.com.br/last/USD-BRL'

try:
    response = requests.get(url)

    if response.status_code == 200:
        dados_conversao = response.json()
        cotacao_atual = dados_conversao['USDBRL']
        valor = float(cotacao_atual['bid'])

        print('\n=== Valor cotação do Dólar Americano para o Real Brasileiro: ===')
        print(f'O valor para compra atual Dólar em Reais é: R$ {valor:.2f}')
    else:
        print(f'Ocorreu um erro no acesso da API. Código: {response.status_code}')
except requests.exceptions.RequestException as e:
    print(f'Ocorreu um erro: {e}')