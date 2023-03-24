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