##This is a program to generate random dice rolls.  Intended specifically for tabletop RPGs (if, like me, you're moving and have no idea where you packed your dice), but feel free to use it for whatever.  As long as that whatever involves rolling dice.



from random import choice
from random import randint

#This allows the user to put in how many dice they want to roll, and what type.
#I'd like to change this so they can eventually put in d6, d4, etc. instead of just the random number of sides.  Then the question can simply read "What kind of die would you like to roll?

def dice_roll():
    rolls = int(raw_input ("How many dice would you like to roll? "))
    die = raw_input ("How many sides or what type of die would you like to roll? ")
    if die == 'fudge' or die == 'Fudge':
        x = int(float(rolls))
        for i in range (x):
            fudge_roll()
    else:
        x = int(float(rolls))
        for i in range (x):
            number_roll(die)



##For using Fudge dice (FATE System)

def fudge_roll():
    print choice(["+","-","0"])


##For rolling numbered dice

def number_roll(die):
    die = int(float(die))
    if die >= 2:
        print randint(1, die)
    else:
        print "Sorry, I don't think that's a thing."


##This causes the program to execute when you call it from the regular command line

dice_roll()


##Written by Alex Beal for Python 2.7
##Share away, but please leave credit
