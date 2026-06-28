from datetime import date
class ContaBancária:
    def __init__(self, nome, idade, saldo,*, cpf, data, endereco):
        self.nome = nome
        self.saldo = saldo
        self.DataDeNascimento = data.split('/')
        self.DiaDoNascimento, self.MesDoNascimento, self.AnoDoNascimento = data.split('/')
        self.cidade, self.estado = endereco.split()
        self.endereco = endereco
        self.somadeposito=0
        self.somasaque=0
        self.Cpf = cpf
        self.saquesRestantes = 3
        self.nome = nome
        self.idade = idade
        self.Saques = []
        self.depositos = []
    def Depositar(self, *valor):
            m = float(sum(i for i in valor if isinstance(i, (int, float))))
            if m > 0:
                self.saldo += m
                self.somadeposito += m
                self.depositos.append((f'+R${m}', date.today().day, date.today().month, date.today().year))
                print(f'Depositado com sucesso, saldo atual: {self.saldo}')
            else:
                print('inválido, deve depositar um valor positivo!')

    def Sacar(self, **saque):
        s = saque['valor']
        if s <= 500 and self.saquesRestantes != 0 and s < self.saldo:
            self.saldo -= s
            self.somasaque += s
            self.Saques.append((f'-R${s}', date.today().day, date.today().month, date.today().year))
            self.saquesRestantes -= 1
            print(f'Saque completo, saldo atual: {self.saldo}')
        elif self.saquesRestantes != 0:
            print('o limite de saques é R$500')
        elif self.saquesRestantes == 0:
            print('você atingiu o numero máximo de saques diários!')
        else:
            print('seu saldo é insuficiente!')

    def PrintSaldo(self, *Anotações, **extrato):
        print('\n'.join(Anotações))
        if 'show' in extrato.keys():
            for k, v in self.conta.items():
                if 'DateOfExtract' not in extrato.keys():
                    if type(v) == str or type(v) == int or type(v) == float:
                        print(f'{k}: {v}')
                    else:
                        c = 1
                        for i in v:
                            print(f'{c}° {k}: {i[0]}')
                            c += 1
                else:
                    day = extrato['DateOfExtract'][0]
                    month = extrato['DateOfExtract'][1]
                    year = extrato['DateOfExtract'][2]
                    if isinstance(v, (str, int, float)):
                        print(f'{k}: {v}')
                    else:
                        found=False
                        for i in v:
                            if day - i[1] == 0 and month - i[2] == 0 and year - i[3] == 0:
                                found=True
                                c = 1
                                print(f'{c}° {k}: {i[0]}')
                                c += 1
                        if not found:
                            print('não encontrado')
        else:
            d = sum (i for i in self.somadeposito )
            s = sum (i for i in self.somasaque )
            return f'''
depósitos = R${d}
saques = R${s}
Total: {d - s}
'''
    def main(self):
        while True:
            print(f'''
Bem-vindo ao banco Santander
saldo: {self.saldo}
1-Depositar
2-sacar (saques diarios restantes {self.saquesRestantes})
3-extrato
4-sair''')
            ask = input('>>>')
            if ask == '1':
                self.Depositar(float(input('Digite a quantidade a ser depositada: ')))
            elif ask == '2':
                self.Sacar(valor=float(input('Digite a quantidade a ser sacada: ')))
            elif ask == '3':
                self.PrintSaldo(show=True)
            elif ask == '4':
                print('Até logo!')
                break

conta = ContaBancária('Artur', 30, 3000, cpf=40028922, data='11/07/2013', endereco='crisciuma SC')
def ArmazenarContas():
    ls = []
    for c, v in globals().items():
        if isinstance(v, ContaBancária):
            if v.Cpf in ls:
                pass
            else:
                ls.append((v.Cpf, v.nome, v.DataDeNascimento, v.endereco))
    return ls
