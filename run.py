import random


class Board:
    def __init__(self, size, num_ships, board_type):
        self.size = [["*" for x in range(size)] for y in range(size)]
        self.num_ships = ["@" for x in range(num_ships)]
        self.board_type = board_type
        self.guesses = []

    def assign_ships(self):
        """
        Gets a random space on the board and place a ship in that space.
        If that space already has a ship then it will choose another space
        """
        for ship in self.num_ships:
            # The Code Institute Tutor Support team is
            # credited to the code in this for loop
            rand_index = [random.randint(0, 4), random.randint(0, 4)]
            while self.size[rand_index[0]][rand_index[1]] == ship:
                rand_index = [random.randint(0, 4), random.randint(0, 4)]

            self.size[rand_index[0]][rand_index[1]] = ship

        return self.size


player = Board(5, 4, "player")
computer = Board(5, 4, "computer")
player_board = player.assign_ships()
computer_board = computer.assign_ships()
"""
The ship counters below are credited to the Stack
Overflow page linked in the read me file
"""
player_guess_board = [["*" for x in range(5)] for y in range(5)]


def greeting():
    """
    Greets player when the game is initially run.
    Asks the player for their name
    """
    print("WELCOME TO BATTLESHIP SKIRMISH!")
    user_name = input("What is your Name?\n")

    def player_ready():
        """
        Confirms that the player is ready to play.
        """
        player_ready_choice = input(
            f"Hello {user_name}, if you are ready to play, enter 'y'.\n"
        )

        if player_ready_choice.lower() == "y":
            print("Okay, let's play!\n")
        else:
            player_ready()

    player_ready()

    return user_name


def player_turn(name):
    """
    Allows the player to choose which space to attack.
    If the space has already been attacked, then it will ask for another space.
    """
    try:
        player_row_choice = int(input("Choose a row to attack!\n"))
        player_col_choice = int(input("Choose a column to attack!\n"))
        player_choice = (player_row_choice, player_col_choice)
        if player_choice in player.guesses:
            print("You have already attacked this space.")
            print("Please choose another space.")
            player_turn(name)
        player.guesses.append(player_choice)
        if computer.size[player_choice[0]][player_choice[1]] == "@":
            print(f"{name}: HIT!")
            computer.size[player_choice[0]][player_choice[1]] = "X"
            player_guess_board[player_choice[0]][player_choice[1]] = "X"

        if computer.size[player_choice[0]][player_choice[1]] == "*":
            print(f"{name}: MISS!")
            computer.size[player_choice[0]][player_choice[1]] = "O"
            player_guess_board[player_choice[0]][player_choice[1]] = "O"
    except (ValueError, IndexError):
        print("Please input a number from 0 to 4")
        player_turn(name)


def computer_turn():
    """
    Gets the computer to select a random row and column.
    If the computer has already chosen that space, it will choose another.
    Displays a symbol on the board for a hit or miss accordingly.
    """
    computer_row_choice = random.randint(0, 4)
    computer_col_choice = random.randint(0, 4)
    computer_choice = (computer_row_choice, computer_col_choice)
    if computer_choice in computer.guesses:
        computer_turn()
    computer.guesses.append(computer_choice)

    print(f"The Computer attacked: row {computer_row_choice}, column {computer_col_choice}")

    if player.size[computer_choice[0]][computer_choice[1]] == "@":
        print("Computer: HIT!")
        player.size[computer_choice[0]][computer_choice[1]] = "X"

    if player.size[computer_choice[0]][computer_choice[1]] == "*":
        print("Computer: MISS!")
        player.size[computer_choice[0]][computer_choice[1]] = "O"


def display_boards(name):
    """
    Keeps count of the remaing ships for the player and computer.
    Prints the player board and the computer board to show the player
    their and the compluter's attacks.
    """
    player_ships = sum(x.count("@") for x in player.size)
    computer_ships = sum(x.count("@") for x in computer.size)

    print("-" * 40)
    print(f"{name}'s ships remaining: {player_ships}")
    print(f"{name}'s Board")

    # The print statement below is credited to the Stack
    # Overflow page linked in the read me file

    [print(*row) for row in player.size]
    print("-" * 40)
    print(f"Computer ships remaining: {computer_ships}")
    print("Computer's Board")
    [print(*row) for row in player_guess_board]
    print("-" * 40)


def resume_quit():
    """
    Gives the player the option to quit.
    """
    player_resume = input("Enter any key to continue or 'n' to quit.\n")
    if player_resume.lower() == "n":
        quit()


def run_game():
    """
    Run the game until all player or computer ships are destroyed.
    """
    player_name = greeting()
    print("-" * 40)
    print("The top left corner is row: 0, column: 0")
    print("""
    Key:
    @ - Ship
    X - Hit
    O - Miss
    * - Board Space
    """)

    # The while loop condition below is credited to the Stack
    # Overflow page linked in the read me file

    while (any("@" in row for row in player.size) and
           any("@" in row for row in computer.size)):
        resume_quit()
        display_boards(player_name)
        player_turn(player_name)
        computer_turn()

    if not any("@" in row for row in player.size):
        display_boards(player_name)
        print(f"GAME OVER! Unlucky {player_name}, the computer won.")

    if not any("@" in row for row in computer.size):
        display_boards(player_name)
        print(f"CONGRATULATIONS {player_name.upper()}! You beat the computer.")


run_game()
