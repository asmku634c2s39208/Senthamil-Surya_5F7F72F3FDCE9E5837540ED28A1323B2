






# Define the base class player
class Player:
    def play(self):
        print("the player is playing cricket.")

# Define  the derived class Batsman
class Batsman(Player):
    def play(self):
        print("the batsman is batting.")

# Define the derived class Bowler
class Bowler(Player):
    def play(self):
        print("the bowler is bowling.")

# create objects of bastman and bowler classes
batsman = Batsman()
bowler = Bowler()

# Call the play() method for each object
batsman.play()
bowler.play()