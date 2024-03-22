[![OpenSSF Scorecard](https://api.securityscorecards.dev/projects/github.com/MatthewBuchananAstley/vop/badge)](https://securityscorecards.dev/viewer/?uri=github.com/MatthewBuchananAstley/vop)
[![OpenSSF Best Practices](https://www.bestpractices.dev/projects/8697/badge)](https://www.bestpractices.dev/projects/8697)

# vop

The voice of pinocchio (pinocchia)

A password generator.

Reasonably secure modern passwords can be generated with this software.

Modern passwords have to be (preferably) a random sequence of characters, of sufficient length and should consist of at least one uppercase, one lowercase letter and one special character.

Usage:

./vop -pwl 64 (64 characters max) 

The pw.sh script produces a list of between one and a hundred passwords from which a password can be chosen:

./pw 

The password can also be changed into an url friendly base64 string.

./vop -pwl 64 -b64 1
