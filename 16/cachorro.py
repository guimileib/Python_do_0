'''
Exercício 1: Classe Cachorro
Crie uma classe chamada Cachorro.

No construtor __init__, a classe deve receber um nome e uma raca como parâmetros. Estes devem ser armazenados como atributos.

Crie um método chamado latir() que não recebe parâmetros e simplesmente imprime na tela uma mensagem como "O [nome do cachorro] está latindo: Au au!".

Crie duas instâncias (objetos) diferentes da classe Cachorro e chame o método latir() para cada uma delas.

'''

class Cachorro:
    def __init__(self, nome_cachorro, raca):
        self.nome = nome_cachorro
        self.raca = raca
        self.latindo = False
    
    def latir(self):
        if not self.latindo:
            self.latindo = True
            print(f"O {self.nome} está latindo: Au au!\n")
        else:
            print("Cachorro já estava latindo")
        
cachorro1 = Cachorro('dudu', 'shitsu')
cachorro2 = Cachorro('chapito', 'chihuahua')
cachorro1.latir()
cachorro1.latir()