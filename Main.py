import random

title = "|\|\|\|    N-Back    |/|/|/|"
subtitle = "  'the memory buffer game'  "
length = 2                                              # defaults
range = 3
on = True

def clearScreen():
    print('\n'*100)

def nBack(n, c):
    buffer = []
    streak = True
    count = 0

    while streak:
        count += 1
        r = random.randint(1, c)
        buffer = [r] + buffer
        clearScreen()
        print(str(buffer[0]) + '\n')
        guess = input()

        if (count > n):
            match = (buffer[0] == buffer[n])
            buffStr = ' '.join(str(i) for i in buffer)
            buffer.pop()
            guess = (guess == 'm')
            streak = (match == guess)

            if not streak:
                print("Incorrect: the buffer contains [" + buffStr + "]")

    print("You recalled " + str(count - n) + " matches correctly.")
    print("Play Again?\n[y]    yes\n[n]    no\n")
    again = input()

    if again == 'y':
        nBack(n, c)

def menu():
    clearScreen()
    print(title)
    print(subtitle)
    print("  length: " + str(length) + "   range: " + str(range))
    print("[n]    new game")
    print("[s]    settings")
    print("[i]    instructions")
    print("[q]    quit\n")

    selection = input()

    if selection == 'n':        # new game
        nBack(length, range)

    elif selection == 's':      # settings
        clearScreen()
        newLen = int(input("enter buffer length (1-20): \n"))

        if 1 <= newLen <= 20:
            global length
            length = newLen
        newRan = int(input("enter buffer range (2-9): \n"))

        if 2 <= newRan <= 9:
            global range
            range = newRan

    elif selection == 'i':      # instructions
        clearScreen()
        print("Numbers from 1-"+str(range)+" will be shown one at a time.")
        print("If a number has appeared "+str(length)+" numbers ago,")
        print("enter [m] for memory. \nOtherwise, enter [n] for no.")
        input()

    elif selection == 'q':      # quit
        global on
        on = False

while on:
    menu()

