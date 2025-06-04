#!/usr/bin/env python3

import sys
from collections import Counter

pw = sys.argv[1]
counts = Counter(pw)
total = len(pw)
for char, count in counts.most_common():
    print(f"{repr(char)}: {count} ({count / total:.2%})")
