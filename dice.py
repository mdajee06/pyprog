#Write a function to decide the winner of a dice game. 
# The function takes two integer parameters and returns a string 
# that says who won which should be either “player1” or “player2”.
#  The winner depends on the rolls being odd or even as follows

def checker(play1, play2):
    roll = [1,13]

    play1 = (input("choose two numbers between 1,12?"))
    play2 = (input("chosse two numbers between 1,12?"))


    if roll == [2,4,6,8,10,12]:
        return ("player1")
    elif roll == [1,3,5,7,9,11]:
        return ("player2")
    
print(checker(1,12)) # player 1 wins
print(checker(1,12)) # player 2 wins