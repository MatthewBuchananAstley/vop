[![OpenSSF Scorecard](https://api.securityscorecards.dev/projects/github.com/MatthewBuchananAstley/vop/badge)](https://securityscorecards.dev/viewer/?uri=github.com/MatthewBuchananAstley/vop)
[![OpenSSF Best Practices](https://www.bestpractices.dev/projects/8697/badge)](https://www.bestpractices.dev/projects/8697)

# vop

A password generator.

With this software, reasonably secure modern passwords can be generated.

Modern passwords have to be (preferably) a random sequence of characters, of sufficient length and should consist of at least one uppercase, one lowercase letter and one special character.

# Installation

The application can be installed via the git clone command:

    $git clone https://github.comm/MatthewBuchananAstley/vop.git

# Usage:

    ./vop 64 

The password length be an arbitrarily large number, however keep in mind that passwordfields in many cms databases are constrained to a certain amount of characters.

# Combining fractions of passwords from a list of generated passwords into a new password.

The pw script produces a list of between one and a hundred passwords from which a password can be chosen or combined into a new password with some added manual typing for extra security:

    ./pw 100 

# Other uses 

The password can also be changed into an url friendly base64 string and prepended to publicly accessible files on webservers.

    ./vop 64 1
