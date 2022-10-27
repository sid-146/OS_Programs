import os
import sys

currentPath = os.path.dirname(__file__)
helperPath = os.path.join(currentPath, "..", "helpers")
sys.path.append(helperPath)

import helper

class FCFS():
    pass


class Zero_arrival():
    pass

class Variable_arrival():
    pass

class Pre_Emptive():
    pass

class Non_pre_emptive():
    pass