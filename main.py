class ContaBancária:
    def __init__(self, nome, idade, saldo):
        self.nome = nome
        self.saldo = saldo
        self.saquesRestantes = 3
        self.nome = nome
        self.idade = idade
        self.Saques = []
        self.depositos = []
        self.conta = {
            'ContaDe:':self.nome,
            'saldo': self.saldo,
            'saque': self.Saques,
            'deposito': self.depositos
        }
    def Depositar(self):
            m = float(input('Digite a quantidade a ser depositada: '))
            if m > 0:
                self.saldo += m
                self.depositos.append(f'+R${m}')
                print(f'Depositado com sucesso, saldo atual: {self.saldo}')
            else:
                print('inválido, deve depositar um valor positivo!')
    def Sacar(self):
        s = float(input('Digite a quantidade a ser sacada: '))
        if s <= 500 and self.saquesRestantes != 0 and s < self.saldo:
            self.saldo -= s
            self.Saques.append(f'-R${s}')
            self.saquesRestantes -= 1
            print(f'Saque completo, saldo atual: {self.saldo}')
        elif self.saquesRestantes != 0:
            print('o limite de saques é R$500')
        elif self.saquesRestantes == 0:
            print('você atingiu o numero máximo de saques diários!')
        else:
            print('seu saldo é insuficiente!')

    def PrintSaldo(self):
        for k, v in self.conta.items():
            if type(v) == str or type(v) == int or type(v) == float:
                print(f'{k}: {v}')
            else:
                for i in v:
                    c = 1
                    print(f'{c}° {k}: {i}')
                    c += 1
    def main(self):
        while True:
            print(f'''
Bem-vindo ao banco Santander

1-Depositar
2-sacar (saques diarios restantes {self.saquesRestantes})
3-extrato
4-sair''')
            ask = input('>>>')
            if ask == '1':
                self.Depositar()
            elif ask == '2':
                self.Sacar()
            elif ask == '3':
                self.PrintSaldo()
            elif ask == '4':
                print('Até logo!')
                break

conta = ContaBancária('Artur', 30, 3000)
conta.main()
