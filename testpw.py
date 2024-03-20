#!/usr/bin/python3
#
# SPDX-License-Identifier: Apache-2.0
# FileCopyrightText: <text> 2024 Matthew Buchanan Astley (mbastley@gmail.com, matthewbuchanan@astley.nl) </text>
#    
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License

import os,sys
import unittest
import vop 


class TestPwMethods(unittest.TestCase):

    def getpw(self):
        a = vop.rhsh(int(10))
        a1 = vop.rd(a)
        return(vop.apw(a1))

    def test_pw(self):
        a = self.getpw()
        uc_cnt = 0
        lc_cnt = 0 
        sc_cnt = 0

        for i in a:
            if i.isupper() == True:
                uc_cnt += 1 

        for i in a:
            if i.islower() == True:
                lc_cnt += 1

        for i in a:
            if vop.chkspchr(i) == True:
                sc_cnt += 1 

        err = {}

        err["l_err"] = 0 

        if len(a) == 10:
            print("Ja 10")
        else: 
            print("Fout ", len(a))
            err["l_err"] += 1

        err["uc_err"] = 0

        if uc_cnt >= 1:
            print("Ja", uc_cnt, " ", a)
        else: 
            #print("fout")
            err["uc_err"] += 1

        err["lc_err"] = 0 

        if lc_cnt >= 1:
            print("Ja", lc_cnt, " ", a)
        else:
            err["lc_err"] += 1

        err["sc_err"] = 0

        if sc_cnt >= 1:
            print("Ja", sc_cnt, " ", a)
        else:
            err["sc_err"] += 1
             
        for i in err.keys():
            if err[i] == 0:
                print("PASS")
            else:
                #print("FAIL ", i) 
                exit("FAIL " + i) 
      
if __name__ == '__main__':
    unittest.main()   
