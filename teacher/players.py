from baralhos import Baralho

class Player():
    def __init__(self, name):
        self.name = name
        self.hand = Baralho(3)

    def adicionar(self, carta):
        self.hand.adicionar(carta)

    def __str__(self):
        return str(self.name) + "," + str(self.hand)
        