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
            user_action = input(
                "Press enter to add generation or q to quit or s to save the game state:"
            )

            if user_action == "":
                game.draw_board()
                game.update_board()
            elif user_action == "s":
                self.export_to_file()

    def export_to_file(self):
        """Class method to export the Game state to a file"""
        try:
            file_name = input("Enter filename: ")
        except:
            print("Invalid filename")

        try:
            with open(file_name, "w") as f:
                f.writelines("hello")
        except:
            print("Something is wrong")


if __name__ == "__main__":
    game = Game()
