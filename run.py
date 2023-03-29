import random 

class Board:
    def __init__(self, size, num_ships, type):
        self.size = [["*" for x in range(size)] for y in range(size)]
        self.num_ships = ["@" for x in range(num_ships)]
        self.type = type
    
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

def greeting():
    """
    Greets player when the game is initially run.
    Asks the player for their name.
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

greeting()
player = Board(5, 4, "player")
computer = Board(5, 4, "computer")
player_board = player.assign_ships()
computer_board = computer.assign_ships()
