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
import secrets
import hashlib
import argparse
import base64

#
# pwt

def prpw(a):

    a1 = [] 
    for i in a:
        a1.append(i)
    
    return(a1)

def chknum(a):
    num = [ "0","1","2","3","4","5","6","7","8","9","0"]
    if a in num:
        return(True)

def chkspchr(a):
    spchr = [ '!','@','#','$','%','^','&','*','_','-','+','=','/','?','|'] 
    if a in spchr:
        return(True)

def rtrnlu(a):
    a4 = [ 'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z' ]
    a1 = [ 'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z' ]
    # SystemRandom 8: 7 bytes
    a2 = secrets.SystemRandom("/dev/urandom")
    a3 = a2.randint(0,len(a4) - 1)
    #print("jAAA", a3)
  
    # Chars: possible characters 26 
    if a == "lower":
        return(a4[a3])
    if a == "upper":
        return(a1[a3])
    
class rtrnlU:

    # SystemRandom 9: 7 bytes 
    def upperR():
        a1 = [ 'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z' ]
        a2 = secrets.SystemRandom("/dev/urandom")
        a3 = a2.randint(0,25)
        return(a1[a3])
 
    def lowerR():
        a2 = secrets.SystemRandom("/dev/urandom")
        a3 = a2.randint(0,25)
        a4 = [ 'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z' ]
        return(a4[a3])

    def numbersR():
        a2 = secrets.SystemRandom("/dev/urandom")
        a3 = a2.randint(0,9)
        a4 = [ '0', '1', '2', '3', '4', '5', '6', '7', '8', '9' ]
        return(a4[a3])

   
def apw(a):

    totalchars = len(a)

    a1 = { "upper" : [], "lower" : [], "special" : [], "numbers" : []  } 

    for i in a:
        if i.isupper():
            a1["upper"].append(i)
        elif i.islower():
            a1["lower"].append(i)
        elif chkspchr(i) == True:
            a1["special"].append(i)
        else:
            a1["numbers"].append(i)
            
    a3 = [ "upper", "lower", "special", "numbers" ] 
    a4 = [] 

    #print("JaaA", a1) 

    a5 = {} 

    for ii in a3:
        a5[ii] = len(a1[ii])

    a6 = sorted(a5.values())
             
    print("JaAAaAaAAA", a5)     
    print("JAAAaAAA", a6)

    a7 = [] 
    for iii in a5.keys():
         if a5[iii] == a6[-1]:
    #          print("jaaaA", iii, a5[iii])
              a7.append(iii)
    
    print("jaAaa", a7) 
        
    for e in a3:
        #print("JaAa", e) 
        if len(a1[e]) == 0:
            a4.append(e) 
        for ee in a1[e]:
            a4.append(ee)

    print("JaA", a4)
    #a4.pop() 

    for i in a4:
        if i == "lower":
            a4.append(rtrnlU.lowerR())
            #a4.pop()
            print("JaAaa lower 2", a4)
        if i == "upper":
            a4.append(rtrnlU.upperR())
            #a4.pop()
            print("JaAaaA upper 2", a4)
        if i == "numbers":
            a4.append(rtrnlU.numbersR())
            #a4.pop()
            print("JaaAAAA numbers 3", a4)
      
    print("JAAA", a4)

    if 'lower' in a4: 
        a4.remove("lower")
    if 'upper' in a4:
        a4.remove("upper")
    if 'numbers' in a4:
        a4.remove("numbers")
   
    # SystemRandom 10: 7 bytes 
    a8 = secrets.SystemRandom("/dev/urandom")

    print("JaAaA", a4)

    a8.shuffle(a4)
    print("JaaAAa", a4)   
     
    return(''.join(a4)) 

#
# otp_t

def rspec_char():
    a = [ '!','@','#','$','%','^','&','*','_','-','+','=','/','?','|']
    # SystemRandom 2: 7 bytes
    a1 = secrets.SystemRandom("/dev/urandom")
    # Characters: 15 possible characters
    return(a[a1.randint(0,len(a) -1 )])

def ct():
    a1 = [ 1,1,1,1,1,2,2,2,2,2 ] 
    # SystemRandom 3: 7 bytes
    a = secrets.SystemRandom("/dev/urandom")
    a.shuffle(a1)
    # Chars: possible characters 2
    a2 = a.randint(0,len(a1) - 1)
    return(a1[a2])

def gchr(a):
    a1 = [ 'a', 'b','c','d','e','f' ]
    a2 = [ 'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M', 'N', 'O','P','Q','R','S','T','U','V','W','X','Y','Z' ]
    a8 = [ 0,1,2,3,4,5,6,7,8,9 ]

    # SystemRandom 4: 7 bytes
    a4 = secrets.SystemRandom("/dev/urandom")
    a4.shuffle(a2)

    a7 = [] 
    for a3 in a:
        if a3 in a1:
            #print("JaaaaaA", a4.randint(0,len(a2) -1)) 
            # Chars: possible characters 52 
            a7.append(str(a2[a4.randint(0,len(a2) -1)]))
        elif int(a3) in a8:
            #print("JAaaaaA", a4.randint(0,len(a2) -1)) 
            # Chars: possible characters 10 
            a7.append(str(a8[a4.randint(0,len(a8) -1)]))
    return(''.join(a7))

def pprlwr(a):

    a1 = []
    a2 = int()
    a3 = int()
    a5 = [ 'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z' ]
    a6 = [ 'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z' ]

    for i in a:
        a1.append(i)

    for ii in a1: 
        if ii.isupper():
            a3 += 1
        elif ii.islower():
            a2 += 1
    # SystemRandom 5: 7 bytes 
    a4 = secrets.SystemRandom("/dev/urandom")
    
    # Chars: possible positions = length of password, possible characters = 26  
    if a2 == 0:
        a1[a4.randint(0,len(a1) -1)] = a5[a4.randint(0,len(a5) -1)]

    if a2 == 0:
        a1[a4.randint(0,len(a1) -1)] = a6[a4.randint(0,len(a6) -1)]
         
    a4.shuffle(a1)

    return(a1)

def rd(a):

    a1 = []

    a = gchr(a)
    a = pprlwr(a)

    a2 = [] 

    # SystemRandom 6: 7 bytes
    a6 = secrets.SystemRandom("/dev/urandom")

    for i in a:
        a2.append(a6.randint(0,len(a) - 1))


    a3 = [] 

    for i in a2:
        e4 = ct()
        if e4 == 1:
            a3.append(str(a[i]).upper())
        elif e4 == 2:
            a3.append(str(a[i]).lower())
        else:
            a3.append(str(a[i]))

    # SystemRandom 7: 7 bytes
    #a7 = random.SystemRandom("/dev/urandom")
    a7 = secrets.SystemRandom("/dev/urandom")
    a7.shuffle(a3)
    
    a4 = ''.join(a3)
    a4 = a4.replace(a4[a7.randint(0,len(a4) -1)], str(rspec_char()),1 )

    pw = ''.join(a4)

    return(pw)

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
        a3 = rd(a2)
        print(b64enc(apw(a3)))
    else:
        #a3 = otp_t.rd(a)
        a3 = rd(a)
        print(b64enc(apw(a3)))
