"""
Class for the Whole game
"""

from generation import Generation


class Game:
    """docstring for Game."""

    def __init__(self):
        # assume the user types in a number
        try:
            user_rows = int(input("how many rows? "))
        except:
            print("invalid input for rows")

        try:
            user_columns = int(input("how many columns? "))
        except:
            print("invalid input for columns")

        # create a board:
        game = Generation(user_rows, user_columns)

        # run the first iteration of the board:
        game.draw_board()
        # game_of_life_board.update_board()

        user_action = ""
        while user_action != "q":
            user_action = input("Press enter to add generation or q to quit:")

            if user_action == "":
                game.draw_board()
                game.update_board()


if __name__ == "__main__":
    game = Game()
