'''Implement a class called player that represents a cricket player. The player class should have a
mmeethod called play() which prints "The players is playing cricket. Service a two classes, Batsman and
Bowler, from the player class. Override the play() method in each dervied class to print " the batsman
is batting" and "The blower is blowing", respectively. Write a program to create subjects or both the
Batsman and Bowler classes and call the play() method for each object. '''


 #Define the base class Player
class Player:
     def Player(self):
         print(" The player is playing cricket.")

  #Define the derived class Batsman 
class Batsman(Player):
         def play(self):
             print("The batsman is batting.")

#Define the detived class bowler
class Bowler(Player):
           def play(self):
             print("The bowler is bowling.")

 # create objects of Batsman and Bowler classes
batsman = Batsman() 
bowler = Bowler() 

#call the play() method for each object
batsman.play() 
bowler.play() 