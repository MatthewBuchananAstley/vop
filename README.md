[![OpenSSF Scorecard](https://api.securityscorecards.dev/projects/github.com/MatthewBuchananAstley/vop/badge)](https://securityscorecards.dev/viewer/?uri=github.com/MatthewBuchananAstley/vop)
[![OpenSSF Best Practices](https://www.bestpractices.dev/projects/8697/badge)](https://www.bestpractices.dev/projects/8697)

# vop

A password generator.

With this software, reasonably secure modern passwords can be generated.

Modern passwords have to be (preferably) a random sequence of characters, of sufficient length (minimally 8 usually) and should consist of at least one uppercase, one lowercase letter and one special character or more.

# Installation

The application can be installed via the git clone command:

    $git clone https://github.comm/MatthewBuchananAstley/vop.git

# Usage:

    ./vop 100 

The password length be an arbitrarily large number, however keep in mind that passwordfields in many cms databases are constrained to a certain amount of characters.

# Combining fractions of passwords from a list of generated passwords into a new password.

The pw script produces a list of between one and a hundred passwords from which a password can be chosen or combined into a new password with some added manual typing for extra security:

    ./pw 100 

# In need of more special characters? 

Say no more. Adding more special characters is now possible using the -s flag.

    ./vop -s 10 100

# Other uses 

The password can also be changed into an url friendly base64 string to prepend to a publicly accessible file on a webserver.

    ./vop 64 1

# Not enough special characters?

Here you go, you can use t3 to use the full character set. 

    ./t3 1000

This may cause strange behaviour in other tools such as incorrect character counts, see wc as an example.

# Testing entropy of the passwords 

At first glance the t3 results have more entropy, however some tests have a problem with the character set.

The following tests can be used to check for entropy

    Character_Distribution.py 
    Chi-square_test.py
    Kolmogorov-Smirnov-test.py
    shannon_entropy.py
    
# Checking the quantum safety of your password

A password consisting of 256 bits of entropy is needed to be safe against brute force attacks on your password using quantum computers.

    Character Set Size	Bits/Char	Length for 256 bits
    256 (random bytes)	8		32 characters
    192			7.57		~33.8 characters
    128			7		~36.6 characters
    95 (printable ASCII)6.57		~39.0 characters
    62 (A–Z, a–z, 0–9)	5.95		~43.0 characters

Using vop:

    A minimum password of 39 characters gives ~256 bits of entropy which is sufficient for quantum safety at 128-bit* level 

Using t3:

    A minimum password of 32 characters gives ~256 bits of entropy which is sufficient for quantum safety at 128-bit* level   

You can check the quantum safety of your passwords with Character_Distribution.py:

    ./Character_Distribution.py 

    Character distribution:
    ...
    Î: 1 (1.00%)
    B: 1 (1.00%)
    -: 2 (2.00%)
    ¤: 1 (1.00%)
    K: 2 (2.00%)
    S: 1 (1.00%)
    ...

    Nu­»Õçj(´~ÉîÈ¶³Û}ä£8¸ÍÑXÜôìÒVsY2°}¶á×AÕ²uü4æh¿a,4!áoâÄ+Ì~Oí¸*Ó§Âà\ÝOÂdý=éñc¶¿ìÑ¶Ë;aÆ³+èÉ>mÎBì-¤KS-Kà


    Shannon Entropy: 6.1563 bits per character 

    GREAT QUANTUM SAFE PASSWORD!
   

    Total Entropy: 615.6307 bits (for 100 characters)

* 128 bit level means 2^128 operations which means that it takes so many attempts to crack the password that it will take quantum computers trillions of years
  
