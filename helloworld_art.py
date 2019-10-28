from art import * 

Art=text2art("Hello World",font='block',chr_ignore=True) # Return ASCII text with block font

with open("art.txt", 'w') as f:
    f.write(Art)