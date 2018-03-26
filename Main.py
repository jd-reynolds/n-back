import random

length = 2                                              # defaults
range = 3

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
                clearScreen()
                print("Incorrect: the buffer contains [" + buffStr + "]")

    print("You recalled " + str(count - n) + " matches correctly.")
    print("Play Again?\n[y]    yes\n[n]    no\n")
    again = input()

    if again == 'y':
        nBack(n, c)

nBack(length, range)



