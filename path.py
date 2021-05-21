import sys
import time
import os
import pathlib

def get_path():
    path = os.path.dirname(__file__)
    path = os.path.normpath(path)
    T = path.split(os.sep)
    if len(T) >=10:
        return "Zu Groß"
    elif len(T) == 1:
        sys.path.append(T[0])
        return f"{T[0]}/"
    elif len(T) == 2:
        sys.path.append(str(T[0](T[1])))
        return f"{T[0]}/{T[1]}/"
    elif len(T) == 3:
        sys.path.append(str(T[0](T[1])(T[2])))
        return f"{T[0]}/{T[1]}/{T[2]}/"
    elif len(T) == 4:
        sys.path.append(str(T[0](T[1])(T[2])(T[3])))
        return f"{T[0]}/{T[1]}/{T[2]}/{T[3]}/"
    elif len(T) == 5:
        sys.path.append(str(T[0](T[1])(T[2])(T[3])(T[4])))
        return f"{T[0]}/{T[1]}/{T[2]}/{T[3]}/{T[4]}/"
    elif len(T) == 6:
        sys.path.append(str(T[0](T[1])(T[2])(T[3])(T[4])(T[5])))
        return f"{T[0]}/{T[1]}/{T[2]}/{T[3]}/{T[4]}/{T[5]}/"
    elif len(T) == 7:
        sys.path.append(str(T[0](T[1])(T[2])(T[3])(T[4])(T[5])(T[6])))
        return f"{T[0]}/{T[1]}/{T[2]}/{T[3]}/{T[4]}/{T[5]}/{T[6]}/"
    elif len(T) == 8:
        sys.path.append(str(T[0](T[1])(T[2])(T[3])(T[4])(T[5])(T[6])(T[7])))
        return f"{T[0]}/{T[1]}/{T[2]}/{T[3]}/{T[4]}/{T[5]}/{T[6]}/{T[7]}/"
    elif len(T) == 9:
        sys.path.append(str(T[0](T[1])(T[2])(T[3])(T[4])(T[5])(T[6])(T[7])(T[8])))
        return f"{T[0]}/{T[1]}/{T[2]}/{T[3]}/{T[4]}/{T[5]}/{T[6]}/{T[7]}/{T[8]}/"
