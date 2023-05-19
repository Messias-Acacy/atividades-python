class Pessoa:
    def __init__(self,apelido,peso,idade,andando=False,comendo=False,falando=False):
        self.nome=apelido
        self.peso=peso
        self.idade=idade
        self.andando=andando
        self.comendo=comendo
        self.falando=falando
    
    def Comer(self,comida):
        self.comida=comida
        if self.comendo == False:
            print(f'{self.nome} está comendo {self.comida}')
            self.comendo=True
        else:
            print(f'{self.nome} já está comendo!')

    def PararComer(self):
        if self.comendo == True:
            print(f'{self.nome} parou de comer!')
            self.comendo = False
        else:
            print(f'{self.nome} não pode parar de comer, pois não estava comendo nada')
    
    def Falar(self):
        if self.comendo == True:
            print('Você não pode falar enquanto come')
        elif self.falando == False:
            print(f'{self.nome} está falando!')
            self.falando = True
        else:
            print(f'{self.nome} já está falando!')
    
    def PararFalar(self):
            if self.falando ==True:
                print(f'{self.nome} parou de falar!')
                self.falando = False
            else:
                print(f'{self.nome} Não pode parar de falar, pois já está calado!')
    
    
    def Andar(self):
        if self.andando == False:
            print(f'{self.nome} está andando!')
            self.andando = True
        else:
            print(f'{self.nome} já está andando...')
    
    def PararAndar(self):
        if self.andando == True:
            print(f'{self.nome} parou de andar!')
            self.andando = False
        else:
            print(f'{self.nome} Não parou de andar, pois não estava andando!')



Pessoa1=Pessoa('Kleber',70,52)
print(vars(Pessoa1))
Pessoa1.Comer("Banana")
Pessoa1.Comer('orégano')
Pessoa1.PararComer()
Pessoa1.Comer('orégano')        
Pessoa1.Comer('gengibre')
print('-'*20)
Pessoa1.Falar()
Pessoa1.PararComer()
Pessoa1.Falar()
Pessoa1.Falar()
Pessoa1.PararFalar()
Pessoa1.PararFalar()
print('-'*20)
Pessoa1.Andar()
Pessoa1.Andar()
Pessoa1.PararAndar()
Pessoa1.Andar()
Pessoa1.PararAndar()
Pessoa1.PararAndar()



