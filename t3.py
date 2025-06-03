#!/usr/bin/env python3

import sys
#import random
import secrets 

def replace_non_printables(char_list):
    latin1_printable = [chr(c) for c in list(range(32, 127)) + list(range(160, 256))]
    return [
        c if c in latin1_printable else random.choice(latin1_printable)
        for c in char_list
    ]

def r2(self):
    a = []
    random_bytes = bytes([random.randint(0, 255) for _ in range(self)])
    char_string = random_bytes.decode('latin1')  # One-to-one byte-to-char
    for i in char_string:
        a.append(i)

    filtered_chars = [c for c in a if c.isprintable() and not c.isspace()]
    a1 =replace_non_printables(a)
    print(''.join(a1))

def r3(self):
    a = []
    a1 = secrets.SystemRandom("/dev/urandom")
    random_bytes = bytes([a1.randint(0, 255) for _ in range(self)])
    char_string = random_bytes.decode('latin1')  # One-to-one byte-to-char
    for i in char_string:
        a.append(i)

    filtered_chars = [c for c in a if c.isprintable() and not c.isspace()]
    a2 =replace_non_printables(a)
    #print(''.join(a1))


    latin1_printable = [chr(c) for c in list(range(32, 127)) + list(range(160, 256))]
    cleaned = a2

    if len(a2) < self:
        # Pad with random printable characters
        cleaned += [random.choice(latin1_printable) for _ in range(self - len(cleaned))]
    elif len(cleaned) > self:
        # Truncate
        cleaned = cleaned[:self]

    #return ''.join(cleaned)
    print(''.join(cleaned))
      


def r1():

    charset = ''.join(chr(i) for i in range(256))  # All single-byte characters
    random_bytes = bytes([random.randint(0, 255) for _ in range(100)])
    mapped = ''.join(charset[b] for b in random_bytes)
    print(mapped)

#r2(int(sys.argv[1]))
r3(int(sys.argv[1]))
