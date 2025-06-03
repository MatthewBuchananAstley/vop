#!/usr/bin/env python3

import sys
import numpy as np
from scipy.stats import ks_1samp, uniform

def password_to_values(pw, low=32, high=126):
    values = [ord(c) for c in pw if low <= ord(c) <= high]
    return np.array(values)

def run_ks_test(values, low=32, high=126):
    scaled_values = (values - low) / (high - low)  # normalize to [0, 1]
    D, p_value = ks_1samp(scaled_values, uniform.cdf)
    return D, p_value

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: ./ks_test.py <password_or_random_string>")
        sys.exit(1)

    pw = sys.argv[1]
    values = password_to_values(pw)

    if len(values) < 10:
        print("Not enough data for K-S test (need > 10 valid characters).")
        sys.exit(1)

    D, p = run_ks_test(values)
    print(f"Kolmogorov–Smirnov D: {D:.4f}, p-value: {p:.4f}")
