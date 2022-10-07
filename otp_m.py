#!/usr/bin/python3
#
# 2022 Matthew Buchanan Astley
#

import os,sys
import random 
import hashlib
import otp_t
import argparse
import base64


def process_opts(a):

    try:
        pwlen = a 
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

def b64enc(a3):
        try:
            if int(args.urlsafe_encode) == 1:
                a4 = base64.urlsafe_b64encode(bytes(a3,encoding='utf-8'))
                a5 = str(a4).strip('b\'')
                return(a5)
        except TypeError:
            return(a3)



if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-pwl', '--password_length')
    parser.add_argument('-b64', '--urlsafe_encode')
    args = parser.parse_args()

    print("Ja",args.password_length)
    print("Ja",args.urlsafe_encode)
    pwlen = args.password_length
    process_opts(pwlen)

    a = rhsh(int(pwlen))

    if len(a) == 64:
        a2 = a[0:len(a) -1]
        a2 += str(otp_t.rspec_char()) 
        a3 = otp_t.rd(a2)
        print(b64enc(a3))
    else:
        a3 = otp_t.rd(a)
        print(b64enc(a3))
