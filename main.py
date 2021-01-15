# import modules
from utils.game import Board
from utils.player import Player

print("Hello'o dear user 😄")
print("Welcome to my card game world!")
Play_or_no_Play = input("Would you like to play? (Y/N): ").upper()
print(Play_or_no_Play)
while Play_or_no_Play != "Y" and Play_or_no_Play != "N":
    Play_or_no_Play = input("Since I'm dumb, I only understand 'Y' or 'N': ").upper()

while Play_or_no_Play == "Y":
    print("Creation of the board:")
    nb_of_players = int(input("How many players do you wish: "))
    for i in range(nb_of_players):
        Player()
    new_board = Board(Player.players_list)
    print(new_board)
    new_board.start_game()
    Play_or_no_Play = input(
        "Would you like to play again! 'Y' or any other char to quit: "
    ).upper()

Print("Exiting the game ✋🏽")
