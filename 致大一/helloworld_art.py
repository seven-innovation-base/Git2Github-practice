from art import * 

Art=text2art("Hello World") # Return ASCII text

with open("README.md", 'w') as f:
    f.write(Art)