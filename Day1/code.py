import math
import functools 
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from  AOCHelper import * 
input = []
def readinput():
   global input
   file =  FileHelper()
   input = file.get_arrays_ints_from_separator(readinput_lines("Day1\input.txt"),"\n")
  
def main():
   readinput()
   first_star()
   second_star()

def first_star():
    print("Result First Star")
    print(max(list(map(lambda a: sum(a),input))))
   
def second_star():
    print("Result Second Star")
    print(sum(sorted(list(map(lambda a: sum(a),input)),reverse=True)[:3]))

if __name__ == '__main__':
    main()