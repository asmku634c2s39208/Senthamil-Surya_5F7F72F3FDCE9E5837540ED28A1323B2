






# Define the base class player
class Player:
    def play(self):
        print("the player is playing cricket.")

# Define  the derived class batsman
class Batsman(player):
    def play(self):
        print("the batsman is batting.")

# Define the derived class bowler
class bowler(player):
    def play(self):
        print("the bowler is bowling.")

# create objects of bastman and bowler classes
batsman = Batsman()
bowler = bowler()

#call the play() method for each object
bastman.play()
bowler.play()