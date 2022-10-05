#!/usr/bin/python3

import os,sys
import random

#a = "thevoiceofpinocchio"
#a = sys.argv[1]

def rspec_char():
    a = [ '!','@','#','$','%','^','&','*','_','-','+','=','/','?','|']
    return(a[random.randint(0,len(a) -1 )])

def ct():
    a1 = [ 1,1,1,1,1,2,2,2,2,2 ] 
    random.shuffle(a1)
    a2 = random.randint(0,len(a1) - 1)
    #print(a1[a2])
    return(a1[a2])


def rd(a):

    #a += str(rspec_char())
    a1 = []

    for i in range(0,len(a) -1 ):
        a1.append(i)

    a2 = [] 

    #print("Ja",a1)

    for i in a1:
        a2.append(random.randint(0,len(a1) - 1))

    #print("JAA",a2)

    a3 = [] 

    #for i in range(0,len(a2)):
    for i in a2:
        e4 = ct()
        if e4 == 1:
            a3.append(str(a[i]).upper())
        elif e4 == 2:
            a3.append(str(a[i]).lower())
        
        #print("JaA", a1[i]) 

    #print("JaAA",''.join(str(a3))) 
    a4 = ''.join(a3)
    a4 = a4.replace(a4[random.randint(0,len(a4) -1)], str(rspec_char()),1 )
    
    a5 = []
    e1 = [ 0,1,2,3,4,5,6,7,8,9 ]
    e2 = [ '!','@','#','$','%','^','&','*','_','-','+','=','/','?','|']
    #for i in a4:
    #    if i in e1:
    #        print("ja e1",i)
    #        a5.append(i)
    #    if i in e2:
    #        print("ja e2",i)
    #        a5.append(i)

    #    e3 = ct()

    #    if e3 == 1:
    #        i.upper()
            #a5.append(i.upper())
    #    elif e3 == 2:
    #        i.lower()
            #a5.append(i.lower())

    #print("JaaaA", a4)
    #print("jAAAa", a5)
    #print("JaaAa", ''.join(a5))
    #print("JaaAa", ''.join(a4))
    pw = ''.join(a4)

    return(pw)

#rd(a)
