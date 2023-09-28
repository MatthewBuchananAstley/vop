#!/usr/bin/python3

import os,sys
import time

epoch = sys.argv[1]

def repoch(epoch):

    # normal time from epoch
    normtime = time.localtime(epoch)
    return(time.asctime(normtime))

a = repoch(int(epoch))
print("Ja", a)
