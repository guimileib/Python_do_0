'''
EX2:
Vamos calcular a área de diferentes formas.
Importe o módulo math no início do seu arquivo (import math).
Crie uma classe mãe FormaGeometrica com um método calcular_area() que retorna 0.
Crie duas classes filhas: Retangulo e Circulo.
O __init__ de Retangulo deve receber base e altura. Sobrescreva calcular_area() para retornar self.base * self.altura.
O __init__ de Circulo deve receber raio. Sobrescreva calcular_area() para retornar math.pi * (self.raio ** 2).
Crie uma lista de formas contendo um retângulo e um círculo.
Use um laço for para percorrer a lista e imprimir a área de cada forma, chamando o mesmo método calcular_area() para ambas.
'''


import math

class FormaGeometrica():
    def calcular_area():
        return 0

class Retangulo(FormaGeometrica):
    def __init__(self, base, altura):
        self.b = base
        self.h = altura
    def calcular_area(self):
        return f"Área do retângulo: {self.b * self.h}"

class Circulo(FormaGeometrica):
    def __init__(self, raio):
        self.r = raio
    def calcular_area(self):
        return f"Área do Cículo: {math.pi * (self.r**2)}"
    
r1 = Retangulo(5, 2)
c1 = Circulo(5)

minhas_formas = [r1, c1]

for forma in minhas_formas:
    print(forma.calcular_area())

        