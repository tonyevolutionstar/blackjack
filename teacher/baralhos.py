import random
from cards_teacher import Card

class Baralho:
    def __init__(self, num_cards):
        self.cards = [Card() for _ in range(num_cards)]

    def adicionar(self, carta):
        self.cards.append(carta)

    def buscar(self):
        return self.cards.pop()

    def __str__(self):
        return str(self.cards)
        