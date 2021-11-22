import time
import argparse

class phoneIterator:
    """Iterator that increments based on a wordlist"""

    currLoc = 0 # Number used to keep track of location in iteration


    def __init__(self, staticNum="", maxLen=10, prefix=""):
        """
        staticNum: numbers to default to
        maxLen: maximum length for the number
        prefix: Used to create a prefix like + when a global number is added. Ex, +1 for united states
        """
        self.staticNum = staticNum
        self.genLen = maxLen-len(staticNum)
        self.maxLen = maxLen
        self.prefix = prefix

    def __iter__(self):
        return self

    def __next__(self):
        """
        Increments to the next number and returns a phone number at current iteration
        """
        number = self.generateNum(self.currLoc) # Pass current location to generateNum
        
        self.currLoc += 1 # Increment for next iteration

        return number # Return the phone number

    def generateNum(self, num):
        """
        Generates a phone number at num location
        num: num to create a phone number off of
        """
        line = str(num)
        
        if len(line) > self.genLen:
            raise StopIteration
        
        return self.prefix + self.staticNum + line.ljust(self.genLen, "0")

def writeList(filename, iterator):
    """
    Function that writes to a file using an iterator
    filename: the filename to write the data to
    iterator: iterator object used to get the data to write
    """
    f = open(filename, 'w')

    for i in iterator:
        f.write(i + "\n")

    f.close()

def main():
    parser = argparse.ArgumentParser(description="Creates a wordlist of phone numbers")
    parser.add_argument('--filename', type=str, default="phones.list", help="Filename to write wordlist to.")
    parser.add_argument('--staticnum', type=str, default="", help="First few numbers that stay static. Ex: you want 123******* numbers, pass 123 as argument.")
    parser.add_argument('--len', type=int, default=10, help="Full length of the phone numbers, default is 10")
    parser.add_argument('--prefix', type=str, default="", help="Prefix for the phone numbers, Ex: +1 for US phone numbers")
    parser.add_argument('--benchmark', action="store_true", help="Runs program without writing to disk, used to run a benchmark.")

    args = parser.parse_args()

    iterator = phoneIterator(staticNum=args.staticnum, maxLen=args.len, prefix=args.prefix, )

    if args.benchmark:
        start = time.time()
        for i in iterator:
            i
        stop = time.time()

    else:
        start = time.time()
        writeList(args.filename, iterator)
        stop = time.time()

    print("Took",  stop-start, "Seconds to write file")

if __name__ in '__main__':
    main()
    