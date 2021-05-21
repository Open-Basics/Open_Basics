import sys
import os
import json
import time
from typing import AbstractSet

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

S = get_path()
time.sleep(1)
print(S)
with open(f"{S}files/data.json") as f:
    data = json.load(f)
print(data['Test'])
time.sleep(180)