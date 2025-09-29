'''
Exercício 1: Instrumentos Musicais
Vamos criar um sistema para uma banda.
Crie uma classe mãe Instrumento com um método tocar() que imprime "Tocando um som genérico...".
Crie três classes filhas que herdam de Instrumento: Violao, Bateria e Flauta.
Em cada classe filha, sobrescreva o método tocar() para imprimir uma mensagem específica (ex: "Dedilhando as cordas do violão.", "Batucando na bateria!", "Soprando uma melodia na flauta.").
Crie uma lista chamada minha_banda que contenha uma instância de cada um dos três instrumentos.
Use um laço for para percorrer a lista minha_banda e, para cada instrumento na lista, chame o método instrumento.tocar().
'''

class Instrumento:
    def tocar(self):
        print('Tocando um som genérico...')

class Violao(Instrumento):
    def tocar(self):
        print("Dedilhando as cordas do violão.")

class Bateria(Instrumento):
    def tocar(self):
        print("Batucando na bateria!")

class Flauta(Instrumento):
    def tocar(self):
        print('Soprando uma melodia na flauta.')

violao = Violao()
bateria = Bateria()
flauta = Flauta()

minha_banda = [violao, bateria, flauta]

for instrumento in minha_banda:
    instrumento.tocar()
