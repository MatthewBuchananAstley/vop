#!/usr/bin/env python3
#
# 2025 Matthew Buchanan Astley (matthewbuchanan@astley.nl, mbastley@gmail.com)
#
# A version that outputs even more special characters, made together with ChatGPT.
# It introduces more entropy to the password and more issues with other tools.
# Apparently wc has an issue with these characters and so has the Kolmogorov Smirnov test, this
# results in an exaggerated character count. I catapult fixing wc somewhere on the todo list.
#

import sys
import secrets 
import argparse

class more_special_characters():

    a1 = secrets.SystemRandom("/dev/urandom")
    latin1_printable = [chr(c) for c in list(range(32, 127)) + list(range(160, 256))]

    def replace_non_printables(char_list):
        return [
            c if c in more_special_characters.latin1_printable else more_special_characters.a1.choice(more_special_characters.latin1_printable)
            for c in char_list
        ]


    def r3(self):

        a = []

        random_bytes = bytes([more_special_characters.a1.randint(0, 255) for _ in range(self)])
        char_string = random_bytes.decode('latin1')  # One-to-one byte-to-char
        for i in char_string:
            a.append(i)

        filtered_chars = [c for c in a if c.isprintable() and not c.isspace()]
        a2 = more_special_characters.replace_non_printables(a)


        latin1_printable = [chr(c) for c in list(range(32, 127)) + list(range(160, 256))]
        cleaned = a2

        if len(a2) < self:
            # Pad with random printable characters
            cleaned += [more_special_characters.a1.choice(latin1_printable) for _ in range(self - len(cleaned))]
        elif len(cleaned) > self:
            # Truncate
            cleaned = cleaned[:self]

        return ''.join(cleaned)
      
if __name__ == '__main__':
  
    parser = argparse.ArgumentParser()
    parser.add_argument('Password_Length', metavar='Password Length', nargs=1, type=int, help='int')
    args = parser.parse_args()

    pwlen = args.Password_Length[0]
    
    a = more_special_characters.r3(int(pwlen))
    print(a)

