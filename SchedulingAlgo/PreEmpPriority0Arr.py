from typing import Sequence
from SchedulingAlgo.FCFSVArrivalTime import NumProcess
import random


class CustomPriorityScheduling:
    """
    * This program is made by Sudhanwa Kaveeshwar
    * Program for Preemptive Priority Scheduling with 0 Arrival Time
    ! Info here
    """

    def TakeProcess():
        NumProcess = int(input("Enter number of process: "))

    def TakingData(self, NumProcess: int):
        AllProcessData = []

        for i in range(NumProcess):
            SingleProcessData = []

            ProcessID = int(input("Enter Process ID: "))
            ArrivalTime = 0
            BurstTime = int(input(f"Enter BurstTime of {ProcessID}"))
            Priority = int(input(f"Enter Priorirty of {ProcessID}"))
            IsExecuted = False

            # * SingleProcess [ProcessID, ArrivalTime, BurstTime, Priority, IsExecuted]
            SingleProcessData.extend(
                [ProcessID, ArrivalTime, BurstTime, Priority, IsExecuted])

        AllProcessData.append(SingleProcessData)

        Schedule.SchedulingProcess(self, AllProcessData, NumProcess)

    def SchedulingProcess(self, AllProcessData, NumProcess: int):
        StartTime = []
        ExitTime = []
        STime = 0

        ExecutionSequence = []

        while True:
            ReadyQueue = []
            TempData = []

            for i in range(NumProcess):
                if AllProcessData[i][1] <= STime and AllProcessData[i][4] == False:
                    # * SingleProcess [ProcessID, ArrivalTime, BurstTime, Priority, IsExecuted]
                    TempData.extend(
                        [AllProcessData[i][0], AllProcessData[i][1], AllProcessData[i][2], AllProcessData[i][3]])

                    ReadyQueue.append(TempData)
                    TempData = []

            if len(ReadyQueue) == 0:
                break

            if len(ReadyQueue) != 0:
                #! Sorting According to high number high Priority
                ReadyQueue.sort(lambda x: x[3], reverse=True)
                StartTime.append(STime)


class AutoPriorityScheduling:
    def TakeProcess():
        AutoNumProcess = random.randint(1, 31)

    def TakingData(self, AutoNumProces: int):
        AutoAllProcessData = []

        for i in range(AutoNumProces):
            AutoSingleProcessData = []


if __name__ == "__main__":
    Schedule = CustomPriorityScheduling()
    AutoSchedule = AutoPriorityScheduling()

    print("Do you want to print documentaion")
    decision = input("Enter your decision\n[Y/N] (Default decision is 'NO')")

    if decision.lower() == "y":
        print(Schedule.__doc__)
    else:
        pass

    print("Do you want to test with custom inputs? ")
    Custom = input("Enter your decision\n[Y/N] (Default decision is 'NO')")
    if Custom.lower() == 'y':
        Schedule.TakeProcess()
    else:
        AutoSchedule.TakeProcess()
