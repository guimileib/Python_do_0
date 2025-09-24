"""
EX 1:
Crie um dicionário para representar um perfil de contato. Ele deve conter, no mínimo, as chaves: nome, telefone e email.
Atribua valores para cada uma delas. Em seguida, exiba apenas o nome e o email usando as chaves.
"""

contacts = {
    "nome": "Guilherme ",
    "telefone": "37999645072",
    "email": "guilhermemileib@gmail.com",
}

for contact in contacts:
    print(f"{contact}: {contacts[contact]}")

"""
EX2:
Crie um dicionário que contenha algumas palavras em inglês como chaves e suas traduções para o português como valores.
Peça ao usuário para digitar uma palavra em inglês.
Use essa palavra digitada como chave para acessar e exibir a tradução.
Desafio: Se a palavra não existir no seu dicionário, exiba uma mensagem como "A palavra não está no vocabulário." (Dica: pesquise sobre o método .get() de dicionários, ele é perfeito para isso!).
"""

words = {
    "text": "texto",
    "apple": "maça",
    "bird": "pássaro",
    "library": "biblioteca",
    "ship": "navio",
    "necklace": "colar"
}

user = input("Type a word in english to discover or translation: ")
print()

print(words.get(user, "A palavra não está no vocabulário."))

'''if user == words.get(user):
    print(f"A tradução da palavra digitada é: {words.get(user)}")'''
