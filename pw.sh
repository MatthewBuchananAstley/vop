#!/bin/bash
#
# 2022, 2023 Matthew Buchanan Astley
# To generate a bunch of passwords 


for i in `seq 1 $(shuf -n 1  -i 1-100)`
    do 
       ./otp_m.py -pwl 64
done 
