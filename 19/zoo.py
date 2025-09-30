'''
Exercício 1: Criar a Hierarquia de Classes
Nesta primeira parte, o seu trabalho é apenas definir os "moldes" dos nossos animais.

Crie a classe mãe Animal:
O __init__ deve receber nome e especie.
Deve ter um atributo fome que começa sempre em 100 (100 = com muita fome, 0 = satisfeito).
Crie um método alimentar() que reduz a fome em 25 pontos e imprime uma mensagem de que o animal foi alimentado.
Crie um método emitir_som() que imprime "O animal faz um som genérico.".
Crie as classes filhas:
Crie a classe Leao, que herda de Animal. Sobrescreva o método emitir_som() para imprimir "ROAR!".
Crie a classe Macaco, que herda de Animal. Sobrescreva o método emitir_som() para imprimir "Ugh ugh aah aah!".
Crie a classe Cobra, que herda de Animal. Sobrescreva o método emitir_som() para imprimir "Sssssss!".

'''

class Animal:
    def __init__(self, nome, especie):
        self.nome = nome
        self.especie = especie
        self.fome = 100

    def alimentar(self):
       self.fome = self.fome - 25
       print('O animal foi alimentado')
       if self.fome == 0:
            print('O animal está satisfeito')
            

    def emitir_som(self):
        print('O animal emitiu um som genérico')

class Leao(Animal):
    def __init__(self, nome, especie):
        super().__init__(nome, especie)
    
    def emitir_som(self):
        print('ROAR!')

class Macaco(Animal):
    def __init__(self, nome, especie):
        super().__init__(nome, especie)

    def emitir_som(self):
        print("Ugh ugh aah aah!")

class Cobra(Animal):
    def __init__(self, nome, especie):
        super().__init__(nome, especie)

    def emitir_som(self):
        print("Sssssss!")


leao = Leao('Guilherme','Leão asiático')

