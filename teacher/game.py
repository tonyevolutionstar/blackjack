from baralhos import Baralho
from players import Player

class Game:
    def __init__(self):
        self.player = Player("Jogador1")
        self.croupier = Player("Croupier")
        self.mesa = Baralho(40)
        self._current_player = self.player
        #self.status()

    def status(self):
        print(self.croupier)
        print(self.player)

    def play(self):
        self._current_player.adicionar(self.mesa.buscar())
        #self.status()