import random

class Partida:
    def __init__(self, nome1, peca1, nome2, peca2):
        self.tab = Tabuleiro()
        self.jog1 = Jogador(nome1, peca1)
        self.jog2 = Jogador(nome2, peca2)
        self.jog = random.choice([self.jog1, self.jog2])
        
    def jogada(self):
        print(f"jogador da vez é {self.jog.nome}")
        posy = int(input("qual a linha vc escolhe?")) - 1
        posx = int(input("qual a coluna vc escolhe?")) - 1
            
        self.tab.jogada(posy, posx, self.jog.peca)
        self.jog = self.jog2 if self.jog == self.jog1 else self.jog1

class Tabuleiro:
    def __init__(self):
        self.tabuleiro = [['_','_','_'],
                          ['_','_','_'],
                          ['_','_','_']]

    def draw(self):
        l = 1
        print('  1 2 3')
        for linha in self.tabuleiro:
            print(l, end=' ')
            for celula in linha:
                print(celula, end=' ')
            print()
            l += 1
    
    def jogada(self, posy, posx, peca):
        self.tabuleiro[posy][posx] = peca
        
            
class Jogador:
    def __init__(self, nome, peca):
        self.nome = nome
        self.peca = peca