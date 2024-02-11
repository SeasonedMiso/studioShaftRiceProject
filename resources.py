import psutil
import os
import time
import sys
from kanjiNum import numbersToKanji

from datetime import date, datetime

cpu_usage = psutil.cpu_percent(interval=1)
ram_percent=psutil.virtual_memory().percent

def clear():
    if os.name == 'nt':
        _ = os.system('cls')
    else:
        _ = os.system('clear')

def main():
    #the values it's reading rn are wrong but I think that
    #is because of wsl?
    print("内存 "+numbersToKanji(ram_percent)+"率 ",end='')
    print("中処 "+numbersToKanji(cpu_usage)+"率",end='')
    #print(ram_percent)
    #print(cpu_usage)
if ((len(sys.argv) >1) and (sys.argv[1] == '-r')):
    while True: 
        clear()
        main()
        sys.stdout.flush()
        print("\r"),
        time.sleep(1)
else:
    main()
