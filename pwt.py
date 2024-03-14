#!/usr/bin/python
#
# SPDX-License-Identifier: Apache-2.0
# FileCopyrightText: <text> 2024 Matthew Buchanan Astley (mbastley@gmail.com, matthewbuchanan@astley.nl) </text>
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
import fileinput
#import random
import secrets 

#a = sys.argv[1]

def prpw(a):

    a1 = [] 
    for i in a:
        a1.append(i)
    
    #a1 = a.split()
    #print("JA",a1)
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
    #a2 = random.SystemRandom("/dev/urandom")
    a2 = secrets.SystemRandom("/dev/urandom")
    #a3 = a2.randint(0,len(a) - 1)
    a3 = a2.randint(0,len(a4) - 1)
    #print("jAAA", a3)
  
    # Chars: possible characters 26 
    if a == "lower":
        return(a4[a3])

    if a == "upper":
        return(a1[a3])
    
class rtrnlU:
    #a2 = random.SystemRandom("/dev/urandom")
    #a3 = a2.randint(0,26)

    # SystemRandom 9: 7 bytes 
    def upperR():
        a1 = [ 'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z' ]
        #a2 = random.SystemRandom("/dev/urandom")
        a2 = secrets.SystemRandom("/dev/urandom")
        a3 = a2.randint(0,25)
        return(a1[a3])
 
    def lowerR():
        #a2 = random.SystemRandom("/dev/urandom")
        a2 = secrets.SystemRandom("/dev/urandom")
        a3 = a2.randint(0,25)
        a4 = [ 'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z' ]
        return(a4[a3])
   
def apw(a):

    totalchars = len(a)

    a1 = { "upper" : [], "lower" : [], "special" : [], "numbers" : []  } 
    #a1_isupper = { "upper" : [] }  
    #a1_islower = { "lower" : [] }
    #a1_isSpchr = { "special" : [] }
    #a1_numbers = { "numbers" : [] }

    for i in a:
        if i.isupper():
            #a1_isupper["upper"].append(i)
            a1["upper"].append(i)
        elif i.islower():
            #a1_islower["lower"].append(i)
            a1["lower"].append(i)
        elif chkspchr(i) == True:
            #a1_isSpchr["special"].append(i)
            a1["special"].append(i)
        else:
            #a1_numbers["numbers"].append(i)
            a1["numbers"].append(i)
            
    #a2 = [ a1_isupper["upper"], a1_islower["lower"], a1_isSpchr["special"], a1_numbers["numbers"] ]
   
    a3 = [ "upper", "lower", "special", "numbers" ] 
    a4 = [] 

#    print("JaaA", a1) 
    for e in a3:
#        print("JaAa", e) 
        if len(a1[e]) == 0:
            #print("jaA", a1[e] + " None")
            a4.append(e) 
        
        for ee in a1[e]:
            a4.append(ee)

#    print("JaA", a4)
    for i in a4:
        if i == "lower":
        #    a4.remove(i)
        #    print("JaAaa lower 1", a4)
            #a4.append(rtrnlu("lower"))
            a4.append(rtrnlU.lowerR())
#            print("JaAaa lower 2", a4)
        if i == "upper":
        #    a4.remove(i)
        #    print("JaAaaA upper 1", a4)
            #a4.append(rtrnlu("upper"))
            a4.append(rtrnlU.upperR())
#            print("JaAaaA upper 2", a4)
      
#    print("JAAA", a4)
    if 'lower' in a4: 
        a4.remove("lower")
    if 'upper' in a4:
        a4.remove("upper")

    # SystemRandom 10: 7 bytes 
    #a5 = random.SystemRandom("/dev/urandom")
    a5 = secrets.SystemRandom("/dev/urandom")

    #print("JaAaA", a4)
    a5.shuffle(a4)
    #print("JaaAAa", a4)        
    #return([ a1_isupper, a1_islower, a1_isSpchr, a1_numbers ]) 
    #return([ a1 ]) 
    #return([ ''.join(a4) ]) 
    return(''.join(a4)) 


if __name__ == '__main__':

     for i in fileinput.input(encoding="utf-8"):
        #print("Ja", a)
         ii = i.replace('\n','')
         #print("Ja", i.replace('\n',''))
         #print("jA",prpw(ii))
         print("JAA",apw(ii))
         #print(apw(ii))



