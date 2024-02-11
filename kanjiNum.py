#import psutil
import os
import time
import sys
from datetime import date, datetime

def numConv(num):
    outNum=""
    if(num=="1"):outNum="壱"
    if(num=="2"):outNum="弐"
    if(num=="3"):outNum="参"
    if(num=="4"):outNum="肆"
    if(num=="5"):outNum="伍"
    if(num=="6"):outNum="陸"
    if(num=="7"):outNum="染"
    if(num=="8"):outNum="捌"
    if(num=="9"):outNum="玖"
    if(num=="0"):outNum="零"
    return outNum


def numbersToKanji(item):
    tens = "%d"%(item//10)
    digits = "%d"%(item%10)
    if (tens == "0"):
        tens=""
        convItem = numConv(digits)
    else:convItem = numConv(tens) + "拾" + numConv(digits)
    return convItem

