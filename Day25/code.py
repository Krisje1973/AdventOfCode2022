import math
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from  AOCHelper import * 
input = []
def readinput():
   global input
   input = readinput_lines("Day25\input.txt")
  
def main():
   readinput()
   first_star()
   #second_star()        
          
def first_star():
# Instead of using digits four through zero, the digits are 2, 1, 0, minus (written -), and double-minus (written =). Minus is worth -1, and double-minus is worth -2."
    digits = {"2": 2, "1": 1, "0": 0, "-": -1, "=": -2}
    total=0
    for line in input:
        #111-1==0
        for idx,i in enumerate(line.strip()[::-1]):            
            total += digits[i] * pow(5,idx)

    s = ""
    digits = {v:k for k,v in digits.items()} | { 4:"-", 3:"="}
    while total:
        total, ch = divmod(total,5) #
        total+=ch>2
        s = digits[ch] + s

    print("Result First Star")
    print(s)
def second_star():
    return "NYI"

    print("Result Second Star")

if __name__ == '__main__':
    main()