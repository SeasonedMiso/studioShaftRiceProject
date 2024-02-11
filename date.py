import os
import time
import sys
import re 

from datetime import date, datetime
from kanjiNum import numbersToKanji
from jeraconv import jeraconv 

now = datetime.now()
w2j = jeraconv.W2J()
j2w = jeraconv.J2W()
era = re.split(r'(\d+)', w2j.convert(now.year).split("年")[0])

def clear():
    if os.name == 'nt':
        _ = os.system('cls')
    else:
        _ = os.system('clear')

def main():
    print( era[0] +numbersToKanji(int(era[1])) + numbersToKanji(now.month) + "月　"+ numbersToKanji(now.day)+ "日",end="")

if ((len(sys.argv) >1) and (sys.argv[1] == '-r')):
    while True: 
        clear()
        main()
        sys.stdout.flush()
        print("\r"),
        time.sleep(1)
else:
    main()
