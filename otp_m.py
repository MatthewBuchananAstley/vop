#!/usr/bin/python3
#
# SPDX-License-Identifier: Apache-2.0
# FileCopyrightText: <text> 2022-2024 Matthew Buchanan Astley (mbastley@gmail.com, matthewbuchanan@astley.nl) </text>
#    
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License

import os,sys
import random 
#import secrets
import hashlib
import otp_t
import argparse
import base64
import pwt

def process_opts(a):

    try:
        pwlen = a 
        if int(pwlen) < 8:
            print("usage: otp_m.py [-h] [-pwl PASSWORD_LENGTH] [-b64 URLSAFE_ENCODE]")
            print("Minimum 8 characters, please\n")
            sys.exit()
         
    except TypeError:
        print("usage: otp_m.py [-h] [-pwl PASSWORD_LENGTH] [-b64 URLSAFE_ENCODE]")
        print("Please input pw length\n")
        sys.exit()

def print_mijndate():
    from time import gmtime,strftime
    date = strftime("%Y%m%d.%H%M%S")
    return(date)

def rhsh(pwlen):
    if pwlen >= 64:
        pwlen = 64 


    # SystemRandom 1: 777 bytes
    a = secrets.SystemRandom("/dev/urandom")
    a3 = a.randbytes(777)
    b = str(a3)
    d = hashlib.sha256(b.encode()).hexdigest()
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
    pwlen = args.password_length

    process_opts(pwlen)
    
    a = rhsh(int(pwlen))

    if len(a) == 64:
        a2 = a[0:len(a) -1]
        a3 = otp_t.rd(a2)
        #print(b64enc(a3))
        print(b64enc(pwt.apw(a3)))
    else:
        a3 = otp_t.rd(a)
        #print(b64enc(a3))
        print(b64enc(pwt.apw(a3)))
