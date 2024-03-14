[![OpenSSF Scorecard](htt‌ps://api.securityscorecards.dev/projects/github.com/MatthewBuchananAstley/vop/badge)](htt‌ps://securityscorecards.dev/viewer/?uri=github.com/MatthewBuchananAstley/vop)

# vop

The voice of pinocchio (or pinocchia if you want)

"password generator"

You can now have "The voice of pinocchio or pinocchia" on your computer!
What would the sweet voice of pinoccio or pinocchia provide?

Reasonably secure passwords!

And those consist of at least one uppercase, one lowercase letter and one special character.

usage:

./otp_m.py -pwl 64 (64 characters max) 

The pw.sh script produces a list of between one and a hundred passwords from which a password can be chosen:

./pw.sh 

The password can also be changed into an url friendly base64 string.

./otp_m.py -pwl 64 -b64 1
