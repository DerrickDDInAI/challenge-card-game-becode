# import modules
from utils.player import Player, Deck
from utils.card import Card, Symbol, SYMBOL_LIST, VALUE_LIST


class Board:
    """
    Symbol has 4 attributes: players, turn_count, active_cards, history_cards
    * players: list of Player instances that are playing
    * turn_count: int starting at 0
    * active_cards: list of the last card played by each player
    * history_cards: list of all the cards played since the start of the game, with the exception of active_cards
    """

    def __init__(self, players: list):
        """
        Function that creates an instance of Board class
        """
        self.players = players
        self.turn_count = 0
        self.active_cards = []
        self.history_cards = []

    def __str__(self):
        """
        Function that prints the Board object's attributes 
        """
        return f"{Player.display_players_list()} {self.turn_count} {Deck.format_text_cards_list(self.active_cards)} {Deck.format_text_cards_list(self.history_cards)}"

    def start_game(self):
        """
        Function that 
        * starts the game
        * fill a Deck
        * distribute the cards of the Deck to the players
        * make each Player play() only 1 Card per turn
        * all players have to play at each turn until they have no cards left
        * at the end of each turn, print:
            :the turn count
            :list of active cards
            :number of cards in the history_cards
        """
        # Starts the game
        print("Let's start a new game! May the best win!")

        # Creates the deck, fills and shuffles it
        game_deck = Deck()
        game_deck.fill_deck(SYMBOL_LIST, VALUE_LIST)
        game_deck.shuffle()

        # Distributes the deck to players
        game_deck.distribute()

        # Get the number of possible turns
        total_possible_turns = self.players[0].number_of_cards

        # Makes the players play one card at each turn
        while self.turn_count < total_possible_turns:
            for player in self.players:
                card_played = player.play()
                self.active_cards.append(card_played)
            self.turn_count += 1
            
            # Place the list of active cards in history_cards
            self.history_cards += self.active_cards

            # at each turn, print the turn count, list of active cards and number of cards in the history_cards
            print(f"turn count: {self.turn_count}")
            print(f"active cards: {Deck.format_text_cards_list(self.active_cards)}")
            print(f"history cards: {Deck.format_text_cards_list(self.history_cards)}")

            # resets list of active cards at the end of each turn
            self.active_cards = []


# if the module run is the main program, it performs the following tests:
if __name__ == "__main__":

    player_1 = Player()
    player_2 = Player()
    player_3 = Player()
    print(Player.display_players_list())
    print(Player.count_created_players)
    board_1 = Board(Player.players_list)
    board_1.start_game()
