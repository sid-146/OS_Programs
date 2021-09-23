from SchedulingAlgo.FCFSVArrivalTime import NumProcess
import random


class CustomPriorityScheduling:
    """
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

            #! [ProcessID, ArrivalTime, BurstTime, Priority, IsExecuted]
            SingleProcessData.extend(
                [ProcessID, ArrivalTime, BurstTime, Priority, IsExecuted])

        AllProcessData.append(SingleProcessData)


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
