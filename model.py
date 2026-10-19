import random

class Partida:
    def __init__(self, nome1, peca1, nome2, peca2):
        self.tab = Tabuleiro()
        self.jog1 = Jogador(nome1, peca1)
        self.jog2 = Jogador(nome2, peca2)
        self.jog = random.choice([self.jog1, self.jog2])
        
    def jogada(self):
        posy = int(input("qual a linha vc escolhe?")) - 1
        posx = int(input("qual a coluna vc escolhe?")) - 1
            
        self.tab.jogada(posy, posx, self.jog.peca)

class Tabuleiro:
    def __init__(self):
        self.tabuleiro = [['_','_','_'],
                          ['_','_','_'],
                          ['_','_','_']]

    def draw(self):
        for linha in self.tabuleiro:
            for celula in linha:
                print(celula, end=' ')
            print()
    
    def jogada(self, posy, posx, peca):
        self.tabuleiro[posy][posx] = peca
        
            
class Jogador:
    def __init__(self, nome, peca):
        self.nome = nome
        self.peca = peca