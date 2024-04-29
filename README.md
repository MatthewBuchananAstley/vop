[![OpenSSF Scorecard](https://api.securityscorecards.dev/projects/github.com/MatthewBuchananAstley/vop/badge)](https://securityscorecards.dev/viewer/?uri=github.com/MatthewBuchananAstley/vop)
[![OpenSSF Best Practices](https://www.bestpractices.dev/projects/8697/badge)](https://www.bestpractices.dev/projects/8697)

# vop

A password generator.

Reasonably secure modern passwords can be generated with this software.

Modern passwords have to be (preferably) a random sequence of characters, of sufficient length and should consist of at least one uppercase, one lowercase letter and one special character.

# Installation

The application can be installed via the git clone command:

    $git clone https://github.comm/MatthewBuchananAstley/vop.git

Or with the great snap software distribution system:

    $snap install --devmode --edge voiceofpino

# Usage:

    ./vop -pwl 64 (64 characters max) 

The pw script produces a list of between one and a hundred passwords from which a password can be chosen:

    ./pw 

# Other uses

The password can also be changed into an url friendly base64 string which might be handy to prepend a code to publicly accessible files on webservers.

    ./vop -pwl 64 -b64 1
