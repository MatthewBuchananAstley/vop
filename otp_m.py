#!/usr/bin/python3

import os,sys
import random 
import hashlib
import otp_t

try:
    pwlen = sys.argv[1]
    if int(pwlen) < 8:
        print("Minimum 8 characters, please\n")
        sys.exit()
except IndexError:
    print("Please input pw length\n")
    sys.exit()

def print_mijndate():
    from time import gmtime,strftime
    date = strftime("%Y%m%d.%H%M%S")
    return(date)

def rhsh(pwlen):
    if pwlen >= 64:
        pwlen = 64 

    a = random.SystemRandom("/dev/urandom")
    a3 = a.random()
    b = str(a3)
    c = b.split(".")
    d = hashlib.sha256(c[1].encode()).hexdigest()
    d1 = d[0:int(pwlen)] 
    return(d1)

if __name__ == '__main__':
    a = rhsh(int(pwlen))
    if len(a) == 64:
        a2 = a[0:len(a) -1]
        a2 += str(otp_t.rspec_char()) 
        a3 = otp_t.rd(a2)
        print(a3)
    else:
        a3 = otp_t.rd(a)
        print(a3)
