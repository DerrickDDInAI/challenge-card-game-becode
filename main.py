# import modules
from utils.game import Board
from utils.player import Player, Deck
player_1 = Player()
player_2 = Player()
player_3 = Player()
print(Player.display_players_list())
board_1 = Board(Player.players_list)
board_1.start_game()