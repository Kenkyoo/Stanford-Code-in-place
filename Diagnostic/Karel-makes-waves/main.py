from karel.stanfordkarel import *

def main():
    # TODO: your code here
    while front_is_clear():
        waves()
        go_to_next_beeper()

def waves():
    put_beeper()
    move()
    put_beeper()
    turn_left()
    move()
    put_beeper()
    turn_right()
    safe_move()

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def go_to_next_beeper():
    turn_right()
    move()
    turn_left()
    safe_move()

def safe_move():
    if front_is_clear():
        move()
# don't edit these next two lines
# they tell python to run your main function
if __name__ == '__main__':
    main()