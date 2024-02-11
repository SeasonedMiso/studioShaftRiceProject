#import psutil
import os
import time
import sys

file_name = "necotati.txt"

pipeMode = False;
if (len(sys.argv)>1 and sys.argv[1] == "-p"): pipeMode=True;
with open(file_name) as file:
    i=0
    for line in file:
        print(line.strip(),end='')
        if i == 9 :
            if pipeMode and sys.stdin:
                print("「", end='')
                for pipe in sys.stdin:
                    print(pipe, end='')
                print("」ダニャァ", end='')
            else:
                print("ぶれにゃぁ～",end='')
        print("")
        i+=1
