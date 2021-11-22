import sre_yield
import time

class phoneIterator:
    """Iterator that increments based on a wordlist"""

    currLoc = 0 # Number used to keep track of location in iteration


    def __init__(self, staticNum="", maxLen=10):
        """
        staticNum: numbers to default to
        maxLen: maximum length for the number
        """
        self.staticNum = staticNum
        self.genLen = maxLen-len(staticNum)
        self.maxLen = maxLen

    def __iter__(self):
        return self

    def __next__(self):
        number = self.generateNum(self.currLoc)
        
        self.currLoc += 1

        return number

    def generateNum(self, num):

        line = str(num)
        
        if len(line) > self.genLen:
            raise StopIteration
        
        return self.staticNum + line.ljust(self.genLen, "0")

def generateRegex(text, numLen):
    preSize = len(text)
    output = ""
    for i in text:
        output += "[%s]"%i

    output += "[0-9]"*(numLen-preSize)
    return output

def writeList(filename, iterator):
    f = open(filename, 'w')

    for i in iterator:
        f.write(i + "\n")

    f.close()

def main():
    """iterator = sre_yield.AllStrings(generateRegex("84565", 10).encode())
    
    print(type(iterator), 1)

    start = time.time()
    writeList("phone.list", iterator)
    stop = time.time()

    print("Took ", stop-start)"""


    iterator = phoneIterator(staticNum="123")

    start = time.time()
    writeList("phone.list", iterator)
    stop = time.time()
    print("Took ",  stop-start)

if __name__ in '__main__':
    main()
    