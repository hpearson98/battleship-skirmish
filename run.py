import random 

class Board:
    def __init__(self, size, num_ships, type):
        self.size = [["*" for x in range(size)] for y in range(size)]
        self.num_ships = ["@" for x in range(num_ships)]
        self.type = type
        self.guesses = []

    def assign_ships(self):
        """
        Gets a random space on the board and place a ship in that space.
        If that space already has a ship then it will choose another space
        """
        for ship in self.num_ships:
            # The Code Institute Tutor Support team is credited to the code in this for loop
            rand_index = [random.randint(0, 4),random.randint(0, 4)]
            while self.size[rand_index[0]][rand_index[1]] == ship:
                rand_index = [random.randint(0, 4), random.randint(0, 4)]
            
            self.size[rand_index[0]][rand_index[1]] = ship
            
        return self.size

player = Board(5, 4, "player")
computer = Board(5, 4, "computer")
player_board = player.assign_ships()
computer_board = computer.assign_ships()

def greeting():
    """
    Greets player when the game is initially run.
    Asks the player for their name
    """
    user_name = input("Welcome to Battleship Skirmish!\nWhat is your Name? ")

    def player_ready():
        """
        Confirms that the player is ready to play.
        """
        player_ready_choice = input(f"Hello {user_name}, if you are ready to play press y. ")
        if player_ready_choice.lower() == "y":
            print("Okay, let's play!")
        else:
            player_ready()

    player_ready()

    return user_name

def player_turn():
    """
    Allows the player to choose which space to attack.
    If the space has already been attacked, then it will ask for another space.
    """
    player_row_choice = int(input("Choose a row to attack! "))
    player_col_choice = int(input("Choose a column to attack! "))
    player_choice = (player_row_choice, player_col_choice)
    if player_choice in player.guesses:
        print("You have already attacked this space.")
        print("Please choose another space.")
        player_turn()
    player.guesses.append(player_choice)
    if computer.size[player_choice[0]][player_choice[1]] == "@":
        print("HIT!")
        computer.size[player_choice[0]][player_choice[1]] = "X"
        
    if computer.size[player_choice[0]][player_choice[1]] == "*":
        print("MISS!")
        computer.size[player_choice[0]][player_choice[1]] = "O"
    
def computer_turn():
    """
    Gets the computer to select a random row and column
    """
    computer_row_choice = random.randint(0, 4)
    computer_col_choice = random.randint(0, 4)
    computer_choice = (computer_row_choice, computer_col_choice)
    if computer_choice in computer.guesses:
        computer_turn()
    computer.guesses.append(computer_choice)
    if player.size[computer_choice[0]][computer_choice[1]] == "@":
        print("HIT!")
        player.size[computer_choice[0]][computer_choice[1]] = "X"
        
    if player.size[computer_choice[0]][computer_choice[1]] == "*":
        print("MISS!")
        player.size[computer_choice[0]][computer_choice[1]] = "O"

def display_boards():
    """
    Prints the player board and the computer board
    to show the player their and the compluter's attacks.
    """
    print("-" * 30)
    print("Player's Board")
    """
    The print statement below is credited to the Stack Overflow
    page linked in the read me file
    """
    [print(*row) for row in player.size]
    print("-" * 30)
    print("Computer's Board")
    [print(*row) for row in computer.size]

def run_game():
    player_name = greeting()
    turn = 3
    while turn > 0:
        display_boards()
        player_turn()
        computer_turn()
        turn -= 1

run_game()