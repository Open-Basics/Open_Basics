import sys
import os
import json
import time
from string import ascii_letters
from re import search

cls = lambda: os.system('cls')
cls()

def get_path():
    path = os.path.dirname(__file__)
    path = os.path.normpath(path)
    A = path.split(os.sep)
    if len(A) >=10:
        return "Zu Groß"
    elif len(A) == 1:
        return "International Error | Falscher Ordner"
    elif len(A) == 2:
        sys.path.append(f"{A[0]}/{A[1]}/")
        P = f"{A[0]}/"
        T = P.split("/")
        return f"{T[0]}/"
    elif len(A) == 3:
        sys.path.append(f"{A[0]}/{A[1]}/{A[2]}/")
        P = f"{A[0]}/{A[1]}"
        T = P.split("/")
        return f"{T[0]}/{T[1]}/"
    elif len(A) == 4:
        sys.path.append(f"{A[0]}/{A[1]}/{A[2]}/{A[3]}/")
        P = f"{A[0]}/{A[1]}/{A[2]}/"
        T = P.split("/")
        return f"{T[0]}/{T[1]}/{T[2]}/"
    elif len(A) == 5:
        sys.path.append(f"{A[0]}/{A[1]}/{A[2]}/{A[3]}/{A[4]}/")
        P = f"{A[0]}/{A[1]}/{A[2]}/{A[3]}/"
        T = P.split("/")
        return f"{T[0]}/{T[1]}/{T[2]}/{T[3]}/"
    elif len(A) == 6:
        sys.path.append(f"{A[0]}/{A[1]}/{A[2]}/{A[3]}/{A[4]}/{A[5]}/")
        P = f"{A[0]}/{A[1]}/{A[2]}/{A[3]}/{A[4]}/"
        T = P.split("/")
        return f"{T[0]}/{T[1]}/{T[2]}/{T[3]}/{T[4]}/"
    elif len(A) == 7:
        sys.path.append(f"{A[0]}/{A[1]}/{A[2]}/{A[3]}/{A[4]}/{A[5]}/{A[6]}/")
        P = f"{A[0]}/{A[1]}/{A[2]}/{A[3]}/{A[4]}/{A[5]}/{A[6]}/"
        T = P.split("/")
        return f"{T[0]}/{T[1]}/{T[2]}/{T[3]}/{T[4]}/{T[5]}/"
    elif len(A) == 8:
        sys.path.append(f"{A[0]}/{A[1]}/{A[2]}/{A[3]}/{A[4]}/{A[5]}/{A[6]}/{A[7]}/")
        P = f"{A[0]}/{A[1]}/{A[2]}/{A[3]}/{A[4]}/{A[5]}/{A[6]}/{A[7]}/"
        T = P.split("/")
        return f"{T[0]}/{T[1]}/{T[2]}/{T[3]}/{T[4]}/{T[5]}/{T[6]}/"
    elif len(A) == 9:
        sys.path.append(f"{A[0]}/{A[1]}/{A[2]}/{A[3]}/{A[4]}/{A[5]}/{A[6]}/{A[7]}/{A[8]}/")
        P = f"{A[0]}/{A[1]}/{A[2]}/{A[3]}/{A[4]}/{A[5]}/{A[6]}/{A[7]}/{[A[8]]}/"
        T = P.split("/")
        return f"{T[0]}/{T[1]}/{T[2]}/{T[3]}/{T[4]}/{T[5]}/{T[6]}/{T[7]}/"
    elif len(A) == 10:
        sys.path.append(f"{A[0]}/{A[1]}/{A[2]}/{A[3]}/{A[4]}/{A[5]}/{A[6]}/{A[7]}/{A[8]}/{A[9]}/")
        P = f"{A[0]}/{A[1]}/{A[2]}/{A[3]}/{A[4]}/{A[5]}/{A[6]}/{A[7]}/{[A[8]]}/{A[9]}/"
        T = P.split("/")
        return f"{T[0]}/{T[1]}/{T[2]}/{T[3]}/{T[4]}/{T[5]}/{T[6]}/{T[7]}/{A[8]}/"
    elif len(A) == 11:
        sys.path.append(f"{A[0]}/{A[1]}/{A[2]}/{A[3]}/{A[4]}/{A[5]}/{A[6]}/{A[7]}/{A[8]}/{A[9]}/{A[10]}/")
        P = f"{A[0]}/{A[1]}/{A[2]}/{A[3]}/{A[4]}/{A[5]}/{A[6]}/{A[7]}/{[A[8]]}/{A[9]}/{A[10]}/"
        T = P.split("/")
        return f"{T[0]}/{T[1]}/{T[2]}/{T[3]}/{T[4]}/{T[5]}/{T[6]}/{T[7]}/{A[8]}{A[9]}/"
    elif len(A) == 12:
        sys.path.append(f"{A[0]}/{A[1]}/{A[2]}/{A[3]}/{A[4]}/{A[5]}/{A[6]}/{A[7]}/{A[8]}/{A[9]}/{A[10]}/{A[11]}/")
        P = f"{A[0]}/{A[1]}/{A[2]}/{A[3]}/{A[4]}/{A[5]}/{A[6]}/{A[7]}/{[A[8]]}/{A[9]}/{A[10]}/{A[11]}/"
        T = P.split("/")
        return f"{T[0]}/{T[1]}/{T[2]}/{T[3]}/{T[4]}/{T[5]}/{T[6]}/{T[7]}/{A[9]}/{A[10]}/"

PATH = get_path()
with open(f"{PATH}files/data.json") as f:
    data = json.load(f)

def progressbar(it, prefix="", size=60, file=sys.stdout):
    count = len(it)
    def show(j):
        x = int(size*j/count)
        file.write("%s[%s%s] %i/%i\r" % (prefix, "#"*x, "."*(size-x), j, count))
        file.flush()        
    show(0)
    for i, item in enumerate(it):
        yield item
        show(i+1)
    file.write("\n")
    file.flush()
    
def start(filename: str, fileextension: str, directory: str):
    
    if directory == "BOOT":
        pass
    elif directory == "HOME":
        if filename in data['HOME']['LS']:
            r = data['HOME'][f"{filename}.{fileextension}"]
            l = len(r)
            for l in data['HOME'][f'{filename}.{fileextension}']:
                time.sleep(1)
                T = data['HOME'][f'{filename}.{fileextension}'][l]
                print(T)
                if search("print", T):
                    args = T.split("(")
                    arg = args[1].split(")")
                    for i in arg:
                        if i.startswith("'"):
                            i = i[1:]
                            if i.endswith("'"):
                                i = i[:-1]
                                print(i)
                
                
        

    elif directory == "SYSTEM":
        pass
    elif directory == "CONFIG":
        pass
    elif directory == "PAPERBIN":
        pass
    elif directory == "DATAFILES":
        pass
    else:
        return "An Error occured | Directory not Found"


def boot():
    for i in progressbar(range(20), "Calculating: ", 50):
        time.sleep(0.3)
    print("Calculation was successful")
    for i in progressbar(range(6), "Installing:  ", 30):
        time.sleep(0.4)
    print("Installation was successful")
    for i in progressbar(range(30), "Starting:    ", 50):
        time.sleep(0.7)
    print("Booting...")
    time.sleep(2)
    cls()
    

def home():
    C = input("PS Open-Basics/Home> ")
    T = "StackAbuse"
    V = "tack"
    if T.find(V) != -1:
        print("Founded")

start("Test", "ob", "HOME")