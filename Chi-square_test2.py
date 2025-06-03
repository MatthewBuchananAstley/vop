#!/usr/bin/env python3

import sys
from collections import Counter
from scipy.stats import chisquare

# Your password
pw = sys.argv[1]

# Count character frequencies
counts = Counter(pw)

# Observed counts (e.g., 'x': 6, '4': 5, ...)
observed = list(counts.values())

# Expected: all characters occur equally
expected = [sum(observed) / len(observed)] * len(observed)

# Chi-square test
stat, p_value = chisquare(f_obs=observed, f_exp=expected)

print(f"Chi-square statistic: {stat:.2f} p-value: {p_value:.4f}")
#print(f"p-value: {p_value:.4f}")
