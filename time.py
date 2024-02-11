#import psutil
import os
import time
import sys
from datetime import datetime
from kanjiNum import numbersToKanji

#load1,load5,load15 = psutil.getloadavg()
#cpu_usage = (load15/os.cput_count())*100
#ram_percent=psutil.virtual_memory()[2]

def clear():
    if os.name == 'nt':
        _ = os.system('cls')
    else:
        _ = os.system('clear')

def main():
    now = datetime.now()
    print(numbersToKanji(now.hour)+"時", 
            numbersToKanji(now.minute)+"分",
           numbersToKanji(now.second)+"秒",end="")

if ((len(sys.argv) >1) and (sys.argv[1] == '-r')):
    while True: 
        clear()
        main()
        sys.stdout.flush()
        print("\r"),
        time.sleep(1)
else:
    main()
