'''O Objetivo:
Vamos criar um consultor de clima de linha de comando. O programa irá:

1. Perguntar ao usuário o nome de uma cidade.
2. Buscar o clima atual para essa cidade usando uma API online gratuita.
3. Exibir a temperatura e a condição do tempo de forma clara.
4. Salvar cada cidade pesquisada em um arquivo de histórico (historico.txt) com a data e a hora da consulta.

API - Usada:
https://wttr.in/NOME_DA_CIDADE?format=j1


'''

import requests
from datetime import datetime 

def obter_temperatura(cidade):
    try:
        url = f"https://wttr.in/{cidade}?format=j1"
        response = requests.get(url)
        
        response.raise_for_status()
        
        dados_json = response.json()

        info_clima = {
            'temperatura': dados_json['current_condition'][0]['temp_C'],
            'condicao': dados_json['current_condition'][0]['weatherDesc'][0]['value'],
            'cidade_encontrada': dados_json['nearest_area'][0]['areaName'][0]['value']
        }
        return info_clima
        
    except requests.exceptions.RequestException as e:
       print(f'Ocorreu um erro: {e}')
       return None
    except requests.HTTPError as e:
       print(f'Ocorreu um erro de requisição: {e}')
       return None

def salvar_historico(cidade_pesquisada, dados_clima):
    data_hora_atual = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    with open ('historico.txt' , 'a', encoding='utf-8') as f:
        linha = (f"{data_hora_atual} | Cidade pesquisada: '{cidade_pesquisada}', "
            f"Encontrado: '{dados_clima['cidade_encontrada']}', "
            f"Temp: {dados_clima['temperatura']} °C\n")
        f.write(linha)

def main():
    print('######### CONSULTOR TEMPO #########')
    nome_cidade = input("Digite o nome da cidade: ")
    dados_clima = obter_temperatura(nome_cidade)
    if dados_clima:
        print("\n--- Resultado ---")
        print(f"Clima para: {dados_clima['cidade_encontrada']}")
        print(f"Temperatura atual: {dados_clima['temperatura']}°C")
        print(f"Condição do Tempo: {dados_clima['condicao']}")
        
        salvar_historico(nome_cidade, dados_clima)
        print("\nBusca salva no histórico.")


if __name__ == '__main__':
    main()






