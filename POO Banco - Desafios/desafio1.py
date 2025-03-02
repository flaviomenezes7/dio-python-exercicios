''' 
Para ler e escrever dados em Python, utilizamos as seguintes funções: 
- input: lê UMA linha com dado(s) de Entrada do usuário;
- print: imprime um texto de Saída (Output), pulando linha.  
'''

# Definição da classe ContaBancaria
class ContaBancaria:
    # Método construtor que inicializa o titular, saldo e lista de operações
    def __init__(self, titular):
        self.titular = titular
        self.saldo = 0
        self.operacoes = []

    # Método para depositar um valor na conta
    def depositar(self, valor):
        self.saldo += valor
        self.operacoes.append(f"+{valor}")

    # Método para sacar um valor da conta
    def sacar(self, valor):
        if self.saldo + valor >= 0:
            self.saldo += valor
            self.operacoes.append(str(valor))
        else:
            self.operacoes.append("Saque não permitido")

    # Método para imprimir o extrato da conta
    def extrato(self):
        operacoes_str = ", ".join(self.operacoes)
        print(f"Operações: {operacoes_str}; Saldo: {self.saldo}")

# Leitura do nome do titular da conta
nome_titular = input().strip()  
# Criação de uma instância da classe ContaBancaria
conta = ContaBancaria(nome_titular)  

# Leitura das transações de entrada
entrada_transacoes = input().strip() 
# Conversão das transações de entrada para uma lista de inteiros
transacoes = [int(valor) for valor in entrada_transacoes.split(",")]  

# Processamento das transações
for valor in transacoes:
    if valor > 0:
        conta.depositar(valor)  # Depósito se o valor for positivo
    else:
        conta.sacar(valor)  # Saque se o valor for negativo

# Impressão do extrato da conta
conta.extrato()