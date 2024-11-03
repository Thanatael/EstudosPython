# Hangman Game (Jogo da Forca) 
# Programação Orientada a Objetos

# Import
import random
from os import system, name

# Função para limpar a tela a cada execução
def limpa_tela():
    
     # Windows
     if name == 'nt':
          _ = system('cls')
     # Linux e MacOS
     else:
          _ = system('clear')

# Board (tabuleiro)
board = ['''

>>>>>>>>>>Hangman<<<<<<<<<<

+---+
|   |
    |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
|   |
    |
    |
=========''', '''

 +---+
 |   |
 O   |
/|   |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/    |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/ \  |
     |
=========''']


# Classe
class Hangman:

	# Método Construtor
     def __init__(self, palavra):
          self.palavra = palavra
          self.letras_erradas = []
          self.letras_escohlidas = []

	# Método para adivinhar a letra
     def guess(self, letra):

          if letra in self.palavra and letra not in self.letras_escohlidas:
               self.letras_escohlidas.append(letra)

          elif letra not in self.palavra and letra not in self.letras_erradas:
               self.letras_erradas.append(letra)
          else:
               return False
          
          return True
	
	# Método para verificar se o jogo terminou
		
	# Método para verificar se o jogador venceu
		
	# Método para não mostrar a letra no board
		
	# Método para checar o status do game e imprimir o board na tela
     print("oi")