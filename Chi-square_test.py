#!/usr/bin/env python3

import sys
from collections import Counter
from scipy.stats import chisquare

pw = sys.argv[1]

counts = Counter(pw)
expected = [len(pw) / len(counts)] * len(counts)
observed = list(counts.values())

stat, p_value = chisquare(observed, expected)
print(f"Chi-square: {stat:.2f}, p-value: {p_value:.4f}")
