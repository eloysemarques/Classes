class Conta_Bancaria:
    def __init__ (self, numero_da_conta, saldo, titular):
        self.numero_da_conta = numero_da_conta
        self.saldo = saldo
        self.titular = titular 

    def depositar (self): 
        return f'{self.numero_da_conta} está depositando dinheiro'
    def sacar (self): 
        return f'{self.titular} está sacando dinheiro'
    def saldo_atual (self):
        return f'{self.saldo} este é o saldo atual'
    
    
if __name__ == "__main__":
     conta = Conta_Bancaria ("04012008","13000", "Elisa")
     print(conta.depositar())
     print(conta.sacar())
     print(conta.saldo_atual())
    