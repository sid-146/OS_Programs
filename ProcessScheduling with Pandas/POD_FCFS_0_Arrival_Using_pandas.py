import helper
import pandas as pd
import random
import sys
import os

# when you need to tell folder file where to look for the particular file
currentPath = os.path.dirname(__file__)
helperPath = os.path.join(currentPath, "..", "helpers")
sys.path.append(helperPath)

# from helper import


class FCFS:

    # def __init__(self) -> None:
    #     pass
    """
    This is a POC for using Pandas for Scheduling Algorithm
    Algorithm -> First Come First Serve With 0 Arrival Time
    """

    def TakingData(self):
        pass

    def FCFS_process():
        pass

    def checkTimeTaken():
        pass


class randomFCFS(FCFS):
    def takingRandomData():
        pass


#! Main Function
if __name__ == "__main__":
    NumProcess = helper.ProcessNumber()
    ShowDf = helper.showDataFrames()

    fcfs = FCFS()
    randomfcfs = randomFCFS()
    default = "default 'yes'"
    processNumber = None

    #! Create for only yes and no if other show error
    choiceDoc = str(input(f"Print Docs? [y/n]:\n {default}"))
    if choiceDoc.lower() != "n":
        print("running doc")
        print(fcfs.__doc__)
    else:
        pass

    choiceRandom = str(
        input(f"Use Random  Number for FCFS [y/n]:\n{default} "))
    if choiceRandom.lower() != "n":
        choiceCustomProcess = input(
            f"Use random Number Process [y/n]:\n{default}")
        if choiceCustomProcess.lower() != "n":
            #! to import of helper
            numberProcess = NumProcess.getRandomProcessNumber()
            print(numberProcess)
