from art import * 

Art=text2art("Hello World") # Return ASCII text

with open("README.rst", 'w') as f:
    f.write(Art)