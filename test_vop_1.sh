#!/bin/bash
#
# SPDX-License-Identifier: Apache-2.0
# FileCopyrightText: <text> 2025 Matthew Buchanan Astley (mbastley@gmail.com, matthewbuchanan@astley.nl) </text>
# Script to test if the pw string contains the required amount of characters


rfile=$(date '+%Y%m%d%H%M%S')
pwl=$1

if [ -z $pwl ] ; then
    echo "Please provide the password length"
    exit 2
fi

function cleanr() {
    #
    # On sigint (ctrl c) symlink to the latest results file
    echo "SIGINT!" 
    if [ -e latest_vop_1_results.txt ] ; then
        rm latest_vop_1_results.txt 
        ln -s $(ls -larntf results_* | tail -1 | awk '{print $9}') latest_vop_1_results.txt 
    fi
    exit 1
}

trap cleanr SIGINT


while true ; 
    do 
        a=$(./vop $pwl); 
        #a1=$(echo "$a" | sed -z 's/\n//g'| wc -c) ; 
        a1=$(echo "$a" | tail -1| sed -z 's/\n//g'| wc -c) ; 

        if [ -z $2 ] ; then
            echo "$a" "$a1" ; 
        fi 
           

        if [ $a1 != $pwl ] ; then 
            echo Ja "$a" ; 
            echo "JA $pwl $(echo "$a") "$a1" "$a" $(date '+%Y%m%d%H%M%S')" >> results_$pwl_$rfile.txt  ;
            #rm latest_vop_1_results.txt 
            #ln -s $(ls -larntf results_* | tail -1 | awk '{print $9}') latest_vop_1_results.txt
            exit 2
        fi; 
    done
