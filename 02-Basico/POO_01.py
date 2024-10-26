# 17/10/24
print("Aqui se inicia as aulas do modulo básico")

# Exercicio 01

from math import sqrt

class Rocket():
     
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        
    def move_rocket(self, x_increment=0, y_increment=1):
        self.x += x_increment
        self.y += y_increment
        
    def print_rocket(self):
        print(self.x, self.y)
        

roc1 = Rocket(10,34)
roc1.x
roc1.y
roc1.print_rocket()

roc1.move_rocket(12,44)
roc1.print_rocket()

# Exercício 2 - Crie uma classe chamada Pessoa() com os atributos: nome, cidade, telefone e e-mail. Use pelo menos 2
# métodos especiais na sua classe. Crie um objeto da sua classe e faça uma chamada a pelo menos um dos seus métodos
# especiais.

class Pessoa():
    def __init__(self, nome, cidade, telefone, email):
        self.nome = nome
        self.cidade = cidade
        self.telefone = telefone
        self.email = email
    
    def mudar(self, new_nome, new_cidade, new_telefone, new_email):
        self.nome = new_nome
        self.cidade = new_cidade
        self.telefone = new_telefone
        self.email = new_email

    def __str__(self):
        return "O usuario" + self.nome + "mora na cidade" + self.cidade

Pessoa1 = Pessoa("Roberto", "Vitoria", 92828, "rob@gmail.com")
str(Pessoa1)

Pessoa1.mudar("Roberto", "Sao Paulo", 98765, "rob@yahoo.com")
str(Pessoa1)

# Exercício 3 - Crie a classe Smartphone com 2 atributos, tamanho e interface e crie a classe MP3Player com os 
# atributos capacidade. A classe MP3player deve herdar os atributos da classe Smartphone.

class Smartphone():
    def __init__(self, tamanho, interface):
        self.tamanho = tamanho
        self.interface = interface
    
class MP3Player(Smartphone):
    def __init__(self, capacidade, tamanho="pequeno", interface="Led"):
        self.capacidade = capacidade
        Smartphone.__init__(self, tamanho, interface)

    def print_mp3player(self):
        print("Os valores do mp3: %s %s %s " %(self.capacidade, self.tamanho, self.interface))

dispositivo1 = MP3Player("64 GB")
dispositivo1.print_mp3player()