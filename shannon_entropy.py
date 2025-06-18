#!/usr/bin/env python3
#
# Entropy analysis

import sys
import math
from collections import Counter

def shannon_entropy(s):
    freqs = Counter(s)
    probs = [v / len(s) for v in freqs.values()]
    return -sum(p * math.log2(p) for p in probs)

    #pw = a 
    #print(shannon_entropy(pw))  # Entropy per character


if __name__ == '__main__':
    print(str(sys.argv[1]), shannon_entropy(sys.argv[1]))
