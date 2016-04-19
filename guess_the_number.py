
# all output for the game will be printed in the console
import simplegui
import random
import math
# helper function to start and restart the game
num_range = 100
def new_game():
    # initialize global variables 
    global number_of_guesses
    global secret_number
    global num_range
    number_of_guesses = int(math.ceil(math.log(num_range,2)))
    secret_number = random.randrange(100)
    if number_of_guesses == 7:
        print "new game started range is [0,100)"
        print "number of guesse is 7"
    if number_of_guesses != 7:
        print "new game started Range is " + str(num_range)
        print "Number of guesses is " + str(number_of_guesses)
    
# define event handlers for control panel
def range100():
    global num_range
    global secret_number
    global number_of_guesse
    num_range = 100 
    secret_number = random.randrange(100)
    return secret_number


def range1000():
    global num_range 
    global secret_number
    global number_of_guesses
    num_range = 1000 
    secret_number = random.randrange(1000)
    new_game()
    return secret_number

    
def input_guess(guess):
    global number_of_guesses
    print " "
    print "Guess was " + guess
    number_of_guesses -= 1
    print "Number of remaining guesses is " + str(number_of_guesses)
    
    guess = int(guess)
    if secret_number > guess:
        print "Higher!"
    elif secret_number < guess:
        print "Lower!"
    else:
        print "Correct!"
        new_game()
        
    if number_of_guesses == 0:
        print "You loose!, The number was " +str(secret_number)
        new_game()
    
    print " "
    
# create frame
frame = simplegui.create_frame("lowhigh",200,200)
# register event handlers for control elements and start frame
button_range100 = frame.add_button('range100', range100)
button_range1000 = frame.add_button("range1000", range1000)
button_new_game  = frame.add_button("new game", new_game)
inp = frame.add_input('input guess', input_guess, 100)
# call new_game 
new_game()



