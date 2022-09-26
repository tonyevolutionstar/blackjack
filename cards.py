class Cards:

    def __init__(self):
        self.name_cards = ["Ace", "King","Queen", "Jack" ,"10", "9", "8", "7", "6", "5", "4", "3", "2"]
        self.type_cards = ["hearts", "clubs", "diamonds","spades"]
        self.list_cards = self.make_list_cards(self.name_cards, self.type_cards)
        self.card_value = {"Ace":11, "King":10, "Queen":10, "Jack":10, "10":10, "9":9, "8":8, "7":7, "6":6, "5":5, "4":4, "3":3, "2":2}


    def make_list_cards(self, name_cards, type_cards):
        l_cards = []
        for card in name_cards:
            for type in type_cards:
                l_cards.append(card+" "+type)
        return l_cards

    def print_cards(self):
        print("Cards ", self.list_cards)
        print("Size of the deck:", len(self.list_cards))
                

