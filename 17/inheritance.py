'''
Funcionario e Gerente
Crie uma hierarquia de classes para representar funcionários de uma empresa.

Crie uma classe mãe Funcionario com um __init__ que recebe nome e salario.

Crie um método exibir_dados() na classe Funcionario que imprime o nome e o salário do funcionário.

Crie uma classe filha Gerente que herda de Funcionario.

No __init__ de Gerente, ela deve receber nome, salario e um novo atributo, setor. Lembre-se de usar super().__init__() para inicializar o nome e o salário.

Crie um novo método em Gerente chamado gerenciar() que imprime uma mensagem como "O gerente [nome] está gerenciando o setor de [setor]".

Crie uma instância de Gerente e chame tanto o método exibir_dados() (herdado) quanto o método gerenciar() (próprio).
'''

class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario
    
    def exibir_dados(self):
        print('==== DADOS FUNCIONARIO ====')
        print(f'Nome do funcionário: {self.nome}\nSalário do funcionário: R${self.salario:.2f}')

class Gerente(Funcionario):
    def __init__(self, nome, salario, setor):
        super().__init__(nome, salario)
        self.setor = setor

    def gerenciar(self):
        print(f'O gerente {self.nome} está gerenciando o setor {self.setor}')

g1 = Gerente('Guilherme', 2000, 'Diretor de Projetos')

g1.exibir_dados()

g1.gerenciar()