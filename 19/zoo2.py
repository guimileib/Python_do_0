'''
Exercício 2: Simular o Zoológico
Agora que temos os moldes, vamos criar os animais e fazê-los interagir.
Crie pelo menos uma instância de cada animal: um Leao, um Macaco e uma Cobra. Dê nomes a eles.
Crie uma lista chamada zoo e adicione todos os objetos de animais que você criou a esta lista.
Use um laço for para percorrer a lista zoo. Para cada animal na lista:
Imprima o nome e a espécie do animal.
Chame o método emitir_som() (você verá o polimorfismo em ação aqui!).
Chame o método alimentar().
Imprima o novo nível de fome do animal.
Imprima uma linha de separação (---) para o próximo animal.
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
macaco = Macaco('Shine', 'mico-leão dourado')
cobra = Cobra('Ametista', 'Jararaca')

zoo = [leao, macaco, cobra]

for animal in zoo:
    print(f'Nome: {animal.nome}\nEspécie: {animal.especie}')
    print(f'Nível de fome: {animal.fome}\n')

    print('Som que ele faz:')
    animal.emitir_som()

    animal.alimentar()
    print()