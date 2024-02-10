#import psutil
import os
import time
import sys

file_name = "necotati.txt"
bure_array = ["ブレニャァ～","ブレニャァ～","ブレニャァ～"]

#load1,load5,load15 = psutil.getloadavg()
#cpu_usage = (load15/os.cput_count())*100
#ram_percent=psutil.virtual_memory()[2]

with open(file_name) as file:
    i=0
    for line in file:
        print(line.strip(),end='')
        #print(" | ",end='')
        if i == 9 :
            #print("ぶれにゃぁ～",end='')
            #print(arg,end='')
            for pipe in sys.stdin:
                print(pipe, end='')
        print("")
        i+=1
