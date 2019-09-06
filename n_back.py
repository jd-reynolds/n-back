import random
import sys

def clearScreen():
    print("\n"*100) 

class NBack:
    """A test of working memory"""
    def __init__(self, bufferLength = 3, bufferRange = 2): # default length & range
        self.bufferLength = bufferLength
        self.bufferRange = bufferRange
        self.buffer = []
        self.on = True

    def rot(self):
        newNum = random.randint(0, self.bufferRange)
        self.buffer.append(newNum)
        print(newNum)

    def test(self):
        guess = input() == "m"
        reoccurance = self.buffer[-1] == self.buffer[-self.bufferLength-1]
        if reoccurance == guess:
            return True
        else: 
            return False
    
    def endgame(self):
        clearScreen()
        print("GAME OVER\n")
        print(self.buffer, "\n")
        print(len(self.buffer) - self.bufferLength - 1, "occurences correctly identified\n")

    def run(self):
        clearScreen()
        print("***|**||*||| N-BACK |||*||**|***\n")
        print("if number occured ", self.bufferLength, " back, enter m(emory)")
        print("else, enter n(o)")
        input()
        while self.on:
            clearScreen()
            self.rot()
            if len(self.buffer) > self.bufferLength:
                if self.test() == False:
                    self.on = False
                    self.endgame()
            else: input()
                 

if __name__ == "__main__":
    if len(sys.argv) == 3:
        game = NBack(bufferLength=int(sys.argv[1]), bufferRange=int(sys.argv[2]))
    else:
        game = NBack()
    game.run()
