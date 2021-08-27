# Cryptic.py
# Encrypt The Discord Token by Running This Program
# Authors: jchisholm204
# Date: July 7, 2021

import os
import scrambler

# Variable for storage of the Token
discordToken = "5amp1e.d15c0rd.t0k3n"

# Use the Scramble Function to Encrypt the Token
CrypticToken = scrambler.scramble(discordToken)

# Check to see the token UnEncrypts
Token = scrambler.parse(CrypticToken)

print(f"TOKEN:\n{Token}\nCrypticToken:\n{CrypticToken}\nUnEncrypts:")
print(Token==discordToken)