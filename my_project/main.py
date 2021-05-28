import re
import sys
import os
import json
import time
from string import ascii_letters
from re import search

def backup_copy():
    os.startfile(f"{PATH}docs/copy.bat") #Vorerst eine Kopie von Open_Basics zu E:/Developer_07/Copies/<DATUM><ZEIT>. Muss noch wenn es fertig ist gelöscht werden
    home() #-> muss zu boot() geändert werden

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

with open(f"{PATH}files/logic.json") as l:
    lo = json.load(l)

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
    
def error(error):
    pass

def logic(filename: str, fileextension: str, directory: str, action: str, args=[]):
    if directory == "BOOT":
        pass
    if action == "start":
        r = []
        liste = lo[directory]
        for i in range(len(liste)):
            r.append(liste[i])
        if "print()" in r:
            for i in range(1000):
                if "print()" in r:
                    r.remove("print()")
            lo['HOME'].clear()
            with open(f"{PATH}files/logic.json", "w+") as l:
                json.dump(lo, l, indent=4)
        lo['HOME'].clear()
        with open(f"{PATH}files/logic.json", "w+") as l:
            json.dump(lo, l, indent=4)
        for string in r:
            if string.startswith("local"):
                    splitted = string.split(" ")
                    arg = splitted[2].split("(")
                    arg1 = arg[1].split(")")
                    zuordnung = splitted[1]
                    wert = arg1[0]
                    lo['HOME'].append(f"{zuordnung}={wert}")
                    with open(f"{PATH}files/logic.json", "w+") as l:
                        json.dump(lo, l, indent=4)
            elif string.startswith("print"):
                args = string.split("(")
                arg1 = args[1].split(")")
                if len(args) == 2:
                    arg2 = args[1].split(")")
                    if arg2[0].startswith("'"):
                        arg2[0] = arg2[0][1:]
                        if arg2[0].endswith("'"):
                            arg2[0] = arg2[0][:-1]
                            to_print = arg2[0]
                            print(to_print)
                    else:
                        li = []
                        for i in range(len(lo[directory])):
                            li.append(lo[directory][i])
                        for split in li:
                            sp = split.split("=")
                            if arg1[0] == sp[0]:
                                if sp[1].startswith("'"):
                                    splite = sp[1].split("'")
                                    print(splite[1])
                                else:
                                    print(sp[1])
            elif string.startswith("if"):
                args = string.split(" ")
                arg1 = args[1].split("(")[1]
                arg2 = args[2].split(")")[0]
                arg3 = args[3].split("[")[1]
                argModus = arg3.split("]")[0]
                arg4 = lo[directory]
                arg5 = args[4].split("||")[1]
                for argument in arg4:
                    s = argument.split("=")
                    sType = s[1]
                    sNull = s[0]
                    global sInt
                    sInt = 0
                    if arg1 == sNull:
                        if argModus == "==":
                            #vergleichen
                            if arg2 == sType:
                                if argument == arg5:  
                                    if sInt == 0:
                                        if string == "__do":
                                            sInt += 1
                                            #Do and End
                        elif argModus == "<=":
                            #kleiner oder gleich
                            pass
                        elif argModus == ">=":
                            #größer oder gleich
                            pass
                        else:
                            #error syntax
                            pass
        logic(filename, fileextension, directory, "end", ['JSON'])           
    elif action == "end":
        lo['HOME'].clear()
        with open(f"{PATH}files/logic.json", "w+") as l:
            json.dump(lo, l, indent=4)
        home()

def start(filename: str, fileextension: str, directory: str):
    lo['HOME'].clear()
    with open(f"{PATH}files/logic.json", "w+") as l:
        json.dump(lo, l, indent=4)
    if directory == "BOOT":
        pass
    elif directory == "HOME":
        if filename in data['HOME']['LS']:
            r = data['HOME'][f"{filename}.{fileextension}"]
            l = len(r)
            for l in data['HOME'][f'{filename}.{fileextension}']:
                T = data['HOME'][f'{filename}.{fileextension}'][l]
                if search("print", T):
                    args = T.split("(")
                    arg = args[1].split(")")
                    for i in arg:
                        if i.startswith("'"):
                            i = i[1:]
                            if i.endswith("'"):
                                i = i[:-1]
                                lo['HOME'].append(f"print('{i}')")
                                with open(f"{PATH}files/logic.json", "w+") as l:
                                    json.dump(lo, l, indent=4)
                        else:
                            lo['HOME'].append(f"print({i})")
                            with open(f"{PATH}files/logic.json", "w+") as l:
                                json.dump(lo, l, indent=4)
                elif search("local", T):
                    args = T.split(" ")
                    if len(args) == 4:
                        if args[0] == None:
                            return #an error senden
                        if args[1] == None:
                            return
                        if args[2] == None:
                            return
                        if args[3] == None:
                            return
                        lo['HOME'].append(f"local {args[1]} ({args[3]})")
                        with open(f"{PATH}files/logic.json", "w+") as l:
                            json.dump(lo, l, indent=4)
                elif search("if", T):
                    args = T.split(" ")
                    arg1 = args[1].split("(")
                    arg2 = args[2]
                    arg3 = args[3].split(")")
                    
                    if len(args) == 4:
                        if arg2.startswith("="):
                            argModus = arg2
                            lo['HOME'].append(f"if ({arg1[1]} {arg3[0]}) [{argModus}] ||{arg3[1]}")
                            with open(f"{PATH}files/logic.json", "w+") as l:
                                json.dump(lo, l, indent=4)

                if T == "__do":
                    lo['HOME'].append("__do")
                    with open(f"{PATH}files/logic.json", "w+") as l:
                        json.dump(lo, l, indent=4)
                elif T == "__end":
                    lo['HOME'].append("__end")
                    with open(f"{PATH}files/logic.json", "w+") as l:
                            json.dump(lo, l, indent=4)
                elif T == "__save":
                    logic(filename, fileextension, directory, 'start', ['JSON'])
                
                
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
    home()
    

def home():
    C = input("PS Open-Basics/Home> ")
    if C == "start":
        start("Test", "ob", "HOME")
    else:
        print("")
        home()


backup_copy()