class Actions:
    """
    Possible actions:
        - hit: get one more card 
        - double: double money 
        - stand: no more cards
        - split: if two cards are the same, divide cards into two hands 
        - surrender: give up the hand
    """
    def __init__(self, action):
        if action == "hit":
            pass