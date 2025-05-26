[![OpenSSF Scorecard](https://api.securityscorecards.dev/projects/github.com/MatthewBuchananAstley/vop/badge)](https://securityscorecards.dev/viewer/?uri=github.com/MatthewBuchananAstley/vop)
[![OpenSSF Best Practices](https://www.bestpractices.dev/projects/8697/badge)](https://www.bestpractices.dev/projects/8697)

# vop

A password generator.

With this software, reasonably secure modern passwords can be generated.

Modern passwords have to be (preferably) a random sequence of characters, of sufficient length (minimally 8 usually) and should consist of at least one uppercase, one lowercase letter and one special character.

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

The password can also be changed into an url friendly base64 string and prepended to publicly accessible files on webservers.

    ./vop 64 1

Keep in mind that the larger the character number is, the higher the demands on your computer hardware. 
That means to get a larger password it will take longer for a result to arrive on your screen. 

    time ./vop 1000000
    real	0m25.980s
    user	0m20.280s
    sys	0m5.494s

