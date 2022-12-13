#!/usr/bin/python3
#
# 2022 Matthew Buchanan Astley

import os,sys
import random

#a = "thevoiceofpinocchio"
#a = sys.argv[1]

def rspec_char():
    a = [ '!','@','#','$','%','^','&','*','_','-','+','=','/','?','|']
    return(a[random.randint(0,len(a) -1 )])

def ct():
    a1 = [ 1,1,1,1,1,2,2,2,2,2 ] 
    a = random.SystemRandom("/dev/urandom")
    a.shuffle(a1)
    a2 = a.randint(0,len(a1) - 1)
    return(a1[a2])

def gchr(a):
    a1 = [ 'a', 'b','c','d','e','f' ]
    a2 = [ 'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M', 'N', 'O','P','Q','R','S','T','U','V','W','X','Y','Z' ]
    a8 = [ 0,1,2,3,4,5,6,7,8,9 ]

    a4 = random.SystemRandom("/dev/random")
    a4.shuffle(a2)
    #print("jaAa",a)
    #print("jaA",a2)
    a7 = [] 
    for a3 in a:
        if a3 in a1:
            a7.append(str(a2[a4.randint(0,len(a2) -1)]))
        elif int(a3) in a8:
            a7.append(str(a8[a4.randint(0,len(a8) -1)]))
            
    #print("JAAA",a7) 
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
    
    a4 = random.SystemRandom("/dev/urandom")
    #print("Jaa",a3) 
    #print("JAa",a2) 
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
    #print("JAaA",a)


    a2 = [] 

    a6 = random.SystemRandom("/dev/urandom")
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

    a7 = random.SystemRandom("/dev/urandom")
    a7.shuffle(a3)
    
    a4 = ''.join(a3)
    a4 = a4.replace(a4[a7.randint(0,len(a4) -1)], str(rspec_char()),1 )

    pw = ''.join(a4)

    return(pw)

