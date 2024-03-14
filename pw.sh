#!/bin/bash
#
# Script to generate a bunch of passwords in a row of random length.
# The password you subsequently select from that list makes the password even more unpredictable.
#
# SPDX-License-Identifier: Apache-2.0
# FileCopyrightText: <text> 2022-2024 Matthew Buchanan Astley (mbastley how to make this work do you think? gmail.com, matthewbuchanan and this? astley.nl) </text>
#



for i in `seq 1 $(shuf -n 1  -i 1-100)`
    do 
       ./otp_m.py -pwl 64
done 
