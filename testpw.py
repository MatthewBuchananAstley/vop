#!/usr/bin/python
#
# SPDX-License-Identifier: Apache-2.0
# FileCopyrightText: <text> 2024 - 2025 Matthew Buchanan Astley (mbastley@gmail.com, matthewbuchanan@astley.nl) </text>
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
        return(vop.chstr.prstr(vop.chstr.rhsh(int(10))))

    def chkspchr(self):
        spchr = [ '!','@','#','$','%','^','&','*','_','-','+','=','/','?','|'] 
        if self in spchr:
            return(True)

    def test_pw(self):
        a = self.getpw()
        uc_cnt = 0
        lc_cnt = 0 
        sc_cnt = 0
        gtl = 0

        for i in a:
            if i.isupper() == True:
                uc_cnt += 1 

            if i.islower() == True:
                lc_cnt += 1

            if TestPwMethods.chkspchr(i) == True:
                sc_cnt += 1 
  
            if i.isdigit() == True:
                gtl += 1

        err = {}

        err["l_err"] = 0 

        if len(a) == 10:
            print("Ja aantal karakters: ",len(a))
        else: 
            print("Fout ", len(a))
            err["l_err"] += 1

        err["uc_err"] = 0
        
        if uc_cnt >= 1:
            print("Ja aantal uppercase: ", uc_cnt, " ", a)
        else: 
            #print("fout")
            err["uc_err"] += 1

        err["lc_err"] = 0 

        if lc_cnt >= 1:
            print("Ja aantal lowercase: ", lc_cnt, " ", a)
        else:
            err["lc_err"] += 1

        err["sc_err"] = 0

        if sc_cnt >= 1:
            print("Ja speciaal karakter: ", sc_cnt, " ", a)
        else:
            err["sc_err"] += 1
       
        err["gtl"] = 0 
 
        if gtl >= 1:
            print("Ja getal: ", gtl, " ", a)
        else:
            err["gtl"] += 1 
              
        for i in err.keys():
            if err[i] == 0:
                print("PASS")
            else:
                #print("FAIL ", i) 
                exit("FAIL " + i) 
      
if __name__ == '__main__':
    unittest.main()   
