'''
Veiculo e Sobrescrita de Métodos
Vamos praticar a sobrescrita de métodos.

Crie uma classe mãe Veiculo com um __init__ que recebe marca e modelo.

Na classe Veiculo, crie um método ligar() que imprime "O veículo ligou.".

Crie uma classe filha Carro que herda de Veiculo.

Crie uma classe filha Moto que herda de Veiculo.

Na classe Moto, sobrescreva o método ligar() para que ele imprima "A moto deu a partida com um pedal.".

Crie uma instância de Carro e uma de Moto. Chame o método ligar() em ambas e observe que, apesar de terem o mesmo nome, o comportamento é diferente.

'''

class Veiculo:
    def __init__(self, marca, modelo):
        self.marca = marca 
        self.modelo = modelo
    
    def ligar(self):
        print('O veículo ligou!')

class Carro(Veiculo):
    pass

class Moto(Veiculo):
    def ligar(self):
        print('A moto deu partida no pedal.')

c1 = Carro('Volkswagem', 'Tiguan')
m1 = Moto('Honda', 'Bizz')

c1.ligar()
m1.ligar()