#!/usr/bin/python3
#
# Checker to check quantum safety of passwords, using shannon entropy check
# SPDX-License-Identifier: Apache-2.0
# 2025 Code compiled by ChatGPT, quantum safety check added by Matthew Buchanan Astley (matthewbuchanan@astley.nl, mbastley@gmail.com)
# 

import sys
from collections import Counter
import math

def shannon_entropy(password: str) -> float:
    if not password:
        return 0.0
    length = len(password)
    counts = Counter(password)
    entropy = -sum((count / length) * math.log2(count / length) for count in counts.values())
    return entropy

def character_distribution(password: str):
    counts = Counter(password)
    total = len(password)
    print("Character distribution:")
    for char, count in counts.items():
        printable_char = repr(char)[1:-1]  # escape characters like \n or \t
        print(f"{printable_char}: {count} ({count / total:.2%})")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./character_distribution.py <password>")
        sys.exit(1)
    
    password = sys.argv[1]
    entropy = shannon_entropy(password)
    character_distribution(password)
    print("\n")
    print(password)
    print(entropy)
    print("\n")
    if (entropy * len(password)) < 256:
       print(f"Shannon Entropy: {entropy:.4f} bits per character", "\n")
       print("PASSWORD NOT QUANTUM SAFE!\n\n", f"Total Entropy: {entropy * len(password):.4f} bits (for {len(password)} characters)\n")
    else:
       print(f"Shannon Entropy: {entropy:.4f} bits per character", "\n")
       print("QUANTUM SAFE PASSWORD!\n\n", f"Total Entropy: {entropy * len(password):.4f} bits (for {len(password)} characters)\n")

