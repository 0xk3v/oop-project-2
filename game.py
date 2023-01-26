"""
Class for the Whole game
"""

from generation import Generation


class Game:
    """docstring for Game."""

    def __init__(self):

        self.importer_data = []

        # Game menu
        try:
            print(
                """
            Conway's Game of Life

            Menu:
            1. Import from file
            2. Start Game
            3. Exit\n
            """
            )
            choice = int(input("Enter your choice: "))

            if choice == 1:
                self.import_from_file()
            elif choice == 2:
                try:
                    user_rows = int(input("how many rows? "))
                except:
                    print("invalid input for rows")

                try:
                    user_columns = int(input("how many columns? "))
                except:
                    print("invalid input for columns")

                self.generated = Generation(user_rows, user_columns)

                self.generated.draw_board()

                user_action = ""
                while user_action != "q":
                    user_action = input(
                        "Press enter to add generation or q to quit or s to save the game state:"
                    )

                    if user_action == "":
                        self.generated.draw_board()
                        self.generated.update_board()

                    elif user_action == "s":
                        self.export_to_file()
                    elif choice == 3:
                        exit()
        except:
            print("Invalid choice")

    def export_to_file(self):
        """Class method to export the Game state to a file"""
        self.data_to_export = self.generated.to_str()
        try:
            file_name = input("Enter filename: ")
        except:
            print("Invalid filename")

        try:
            with open(file_name, "w") as f:
                f.writelines(str(self.data_to_export))
        except:
            print("Something was wrong while exporting")

    def import_from_file(self):
        """Class Method to read exported array from a file"""

        # Prompting a user
        try:
            filename = input("Enter file name: ")
            with open(filename, "r") as f:
                self.importer_data = f.readlines()
        except:
            print("Invalid file name")


if __name__ == "__main__":
    game = Game()
