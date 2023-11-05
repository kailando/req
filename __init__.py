moduleNames=open("./requirements.txt", "r").read().splitlines()
for module in moduleNames:
    globals()[module]=__import__(module)
    continue

def Help():
    print("req is a module that imports module names from reqirements.txt in the file's directory. Please make a requirements.txt file containing module names seperated with newlines. Imports on import of this module.")
    return "req is a module that imports module names from reqirements.txt in the file's directory. Please make a requirements.txt file containing module names seperated with newlines. Imports on import of this module."
