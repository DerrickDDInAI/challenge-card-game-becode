# import modules
from utils.card import Card, Symbol, SYMBOL_LIST, VALUE_LIST
from random import (
    choice,
    shuffle,
) 


class Player:
    """
    Player has 5 attributes: name, cards, turn_count, number_of_cards, history
    * name: 
    * cards: list of Card objects that the player has in his hands
    * turn_count: int starting at 0
    * number_of_cards: int starting at 0
    * history: list of Card objects played by the player
    
    And Player class has 2 class attributes: count_created_players, players_list
    * count_created_players: int starting at 0, to count the number of players created
    * players_list: empty list to store the players
    """

    # class attributes
    count_created_players = 0
    players_list = []

    def __init__(
        self,
        name: str = None,
        # cards: list = []
    ):
        """
        Function that creates an instance of Player class
        By default:
        * name is "player_1", then "player_2" if no name is provided
        * the lists cards and history are empty
        * turn_count and number_of_cards are set to 0
        """
        Player.count_created_players += 1
        if name is None:
            self.name = f"player_{Player.count_created_players}"
        else:
            self.name = name

        self.cards = []
        self.turn_count = 0
        self.number_of_cards = 0
        self.history = []
        Player.players_list.append(self)

    def __str__(self):
        """
        Function that prints the Player object's attributes
        """
        return f"{self.name} {Deck.format_text_cards_list(self.cards)} {self.turn_count} {self.number_of_cards} {Deck.format_text_cards_list(self.history)}"

    @classmethod
    def display_players_list(cls):
        """
        Function that prints the player' list
        """
        players_list_displayed = []
        for player in cls.players_list:
            players_list_displayed.append(f"{player.name}")
        return f"{players_list_displayed}"

    def play(self):
        """
        Function that performs the Player's play turn.
        * randomly picks a Card in cards
        * add the Card to the Player's history
        * print: {PLAYER_NAME} {TURN_COUNT} played: {CARD_NUMBER} {CARD_SYMBOL_ICON}

        * return: the Card
        """
        # randomly remove a Cards in cards
        card_picked = choice(self.cards)
        self.cards.remove(card_picked)

        # add the Card to the Player's history
        self.history.append(card_picked)

        # increment the Player's turn count by 1
        self.turn_count += 1

        # decrement the Player's number of cards by 1
        self.number_of_cards -= 1
        
        # if self.number_of_cards == 0:
        # print(f"{self.name} {self.turn_count} has no card")

        # display the play
        print(f"{self.name} {self.turn_count} played: {card_picked}")

        return card_picked


class Deck:
    """
    Deck has 1 attribute: cards
    * cards: list of Card objects
    """

    def __init__(self):
        """
        Function that creates an instance of Deck class
        By default:
        * the list cards is empty
        """
        self.cards = []

    @staticmethod
    def format_text_cards_list(cards_list):
        """
        Static method that format the text of any list of Cards with their attributes
        * return: a list of string
        """
        cards_list_displayed = []
        for card in cards_list:
            cards_list_displayed.append(f"{card}")
        return cards_list_displayed

    def __str__(self):
        """
        Function that prints a list of Cards with their attributes
        """
        return f"{Deck.format_text_cards_list(self.cards)}"

    def __len__(self):
        """
        Function that counts the number of cards in a Deck instance
        """
        return len(self.cards)

    def fill_deck(self, SYMBOL_LIST: list, VALUE_LIST: list):
        """
        Function that fills cards with a complete card game: 
        * cards: list of 52 cards (an instance of 'A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K' for each possible symbol [red ♥, red ♦, black ♣, black ♠])
        """
        for symbol in SYMBOL_LIST:
            for value in VALUE_LIST:
                self.cards.append(Card(symbol.color, symbol.icon, value))

    def shuffle(self):
        """
        Function that shuffles the deck
        """
        shuffle(self.cards)

    def distribute(self):
        """
        Function distributes cards evenly between all the players
        * parameter: Player
        """
        nb_cards_to_distribute_to_each_player = int(
            len(self.cards) / Player.count_created_players
        )
        nb_distributed_cards = 0
        while nb_distributed_cards < nb_cards_to_distribute_to_each_player:
            for player in Player.players_list:
                # randomly gives the player a card
                distributed_card = choice(
                    self.cards
                )  # randomly choose a card from the deck
                self.cards.remove(distributed_card)  # remove that card from the deck
                player.cards.append(distributed_card) # add the card in the play's hands
                # increment by 1 the count of cards the player has in his hands
                player.number_of_cards += 1
            nb_distributed_cards += 1


# if the module run is the main program, it performs the following tests:
if __name__ == "__main__":

    card_1 = Card("black", "♥", 10)
    card_2 = Card("red", "♥", "A")
    print(card_1, card_2)

    ready_player_one = Player()
    print(ready_player_one)
    ready_player_two = Player()
    print(ready_player_two)

    game_deck = Deck()
    game_deck.fill_deck(SYMBOL_LIST, VALUE_LIST)
    print(game_deck)
    print(len(game_deck))
    print(Player.count_created_players)
    game_deck.shuffle()
    print(game_deck)
    game_deck.distribute()

    print(Player.display_players_list())

    print(ready_player_one)
    ready_player_one.play()
    print(ready_player_one)

    print(ready_player_two)
    ready_player_two.play()
    print(ready_player_two)

    ready_player_one.play()
    print(ready_player_one)
