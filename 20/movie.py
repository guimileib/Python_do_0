'''
Este exercício vai revisar: APIs (requests), JSON, e POO (Classes, __init__, Métodos).
Vamos usar a API OMDb (Open Movie Database) para buscar filmes. 
(Atenção: Esta API requer uma chave gratuita. Vá até omdbapi.com/apikey.aspx, selecione a opção "Free", coloque seu e-mail e pegue sua chave).
O objetivo é criar uma Classe que representa um filme.

1. Crie uma classe chamada Filme.

2. O __init__ da classe não deve receber parâmetros, mas deve inicializar os atributos self.titulo, self.ano e self.diretor como None.

3. Crie um método chamado buscar(nome_do_filme, sua_api_key).

4. Dentro deste método, faça uma requisição requests.get para a URL: f"http://www.omdbapi.com/?t={nome_do_filme}&apikey={sua_api_key}".

5. Converta a resposta para JSON.

6. Se a resposta for bem-sucedida ("Response" == "True"), atualize os atributos da classe:

- self.titulo = dados_json['Title']
- self.ano = dados_json['Year']
- self.diretor = dados_json['Director']
- O método deve retornar True.

7. Se a resposta falhar ("Response" == "False"), o método deve retornar False.

8. Crie um método exibir() que imprime os atributos titulo, ano e diretor de forma formatada (só se o título não for None).

9. No código principal:

- Peça ao usuário o nome de um filme.
- Crie um objeto: meu_filme = Filme()
- Chame o método de busca: sucesso = meu_filme.buscar("Nome do Filme", "SUA_CHAVE_AQUI")
- Se sucesso for True, chame meu_filme.exibir().
- Senão, imprima "Filme não encontrado."
'''

# Proximo passo, como pegar os dados um de cada vez na api e como mudar os dados da classe...

import requests

class Filme:
    def __init__(self):
        self.titulo = None
        self.ano = None
        self.diretor = None

    def buscar(self, nome_filme, api_key):
        try:
            response = requests.get(f"http://www.omdbapi.com/?t={nome_filme}&apikey={api_key}")
            dados_json = response.json()

            if dados_json.get("Response") == "True":
                self.titulo = dados_json.get('Title')
                self.ano = dados_json.get("Year")
                self.diretor = dados_json.get("Director")
                return True
            else: 
                return False
            
        except requests.exceptions.RequestException as e:
            print(f"Erro na requisição: {e}")
            return False
        
    def exibir(self):
        if self.titulo is not None:
            print()
            print("Filme Encontrado:")
            print()
            print(f"Título: {self.titulo}")
            print(f"Ano: {self.ano}")
            print(f"Diretor: {self.diretor}")
            print()
        else:
            print("Nenhum filme carregado para exibir")


def main():
    try:
        print("Buscador de Filme")
        print("Dados API Movie")

        nome_filme = input("Digite aqui o nome do filme: ")
        api_key = input("Digite aqui sua chave de API: ")

        meu_filme = Filme()

        print(f'Buscando "{nome_filme}"...')
        sucesso = meu_filme.buscar(nome_filme, api_key)

        if sucesso: 
            meu_filme.exibir()
        else: 
            print("Filme não encontrado")
        
    except Exception as e:
        print(f"Erro inesperado: {e}") 

if __name__ == "__main__":
    main()
