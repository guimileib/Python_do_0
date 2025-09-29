'''
Exercício 2: Classe ContaBancaria
Crie uma classe chamada ContaBancaria.

No construtor __init__, a classe deve receber o titular da conta. O saldo inicial deve ser sempre 0.

Crie um método depositar(valor) que adiciona o valor recebido ao saldo da conta.

Crie um método sacar(valor) que verifica se há saldo suficiente. Se houver, ele subtrai o valor do saldo. Se não houver, ele deve exibir uma mensagem de "Saldo insuficiente".

Crie um método ver_saldo() que imprime o titular e o saldo atual da conta.

Crie uma instância da conta, faça um depósito, tente um saque (um válido e um inválido) e veja o saldo.

'''

class ContaBancaria:
    def __init__(self, titular_conta):
        self.titular = titular_conta
        self.saldo = 0

    def depositar(self, valor):
        self.saldo = valor + self.saldo
        print(f'Você depositou R${valor:.2f}\n')

    def sacar(self, valor):
        
        if self.saldo < valor:
            print('Saldo insuficiente!\n')
        elif self.saldo > 0:
            self.saldo = self.saldo - valor
            print('Saque efetuado com sucesso!\n')

    def ver_saldo(self):
        print(f'====== DADOS DA CONTA: {self.titular} =====')
        print(f" Seu saldo é: R$ {self.saldo:.2f}")
        print('======================================')

conta1 = ContaBancaria('Guilherme')
conta1.depositar(30.00)
conta1.ver_saldo()
conta1.sacar(40.00)

conta1.sacar(20.00)
conta1.ver_saldo()
