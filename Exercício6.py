class Pessoa: 
    def __init__ (self, nome, idade, altura):
        self.nome = nome
        self.idade = idade
        self.altura = altura 

    def informacoes (self): 
        return f'{self.nome}, {self.idade}, {self.altura}, são as informações de {self.nome}'
    def cumprimentar (self): 
        return f'{self.nome} está cumprimentando alguém: Olá, como vai?'
    
if __name__ == "__main__":
     pessoa1= Pessoa ("Eloyse", "17 anos", "1,60")
     print(pessoa1.informacoes())
     print(pessoa1.cumprimentar())