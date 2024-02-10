#import psutil
import os
import time
import sys
from datetime import datetime
#load1,load5,load15 = psutil.getloadavg()
#cpu_usage = (load15/os.cput_count())*100
#ram_percent=psutil.virtual_memory()[2]


def clear():
    if os.name == 'nt':
        _ = os.system('cls')
    else:
        _ = os.system('clear')

def numbersToKanji(hour, minute, second):
    myList = [hour,minute,second]
    outList = []
    def numConv(num):
        outNum=""
        if(num=="1"):outNum="壱"
        if(num=="2"):outNum="弐"
        if(num=="3"):outNum="参"
        if(num=="4"):outNum="肆"
        #change
        if(num=="5"):outNum="五"
        if(num=="6"):outNum="陸"
        if(num=="7"):outNum="染"
        if(num=="8"):outNum="捌"
        #change
        if(num=="9"):outNum="仇"
        if(num=="0"):outNum="零"
        return outNum

    for item in myList:       
        tens = "%d"%(item//10)
        digits = "%d"%(item%10)
        if (tens == "0"):
            tens=""
            convItem = numConv(digits)
        else:convItem = numConv(tens) + "拾" + numConv(digits)
        outList.append(convItem)
    out = outList[0]+"時 "+outList[1]+"分 "+outList[2]+"秒" 
    return out

def main():
    now = datetime.now()
    print(numbersToKanji(now.hour, now.minute, now.second),end="")

if ((len(sys.argv) >1) and (sys.argv[1] == '-r')):
    while True: 
        clear()
        main()
        sys.stdout.flush()
        print("\r"),
        time.sleep(1)
else:
    print("今ノ時間ハ　「",end="")
    main()
    print("」ダニャァ",end="")
