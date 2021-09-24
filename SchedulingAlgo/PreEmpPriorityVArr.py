import random


class CustomPriorityScheduling:
    """
    * this program is made by Sudhanwa Kaveeshwar
    * program for Preemptice priority Scheduling for varying arrival time
    info here!
    """

    def TakingData(self, NumProcess: int):
        AllProcessData = []

        for i in range(NumProcess):
            SingleProcessData = []

            ProcessID = int(input("Enter ProcessID: "))
            ArrivalTime = int(input(f"Enter Arrival Time of {ProcessID}: "))
            BurstTime = int(input(f"Enter BurstTime of {ProcessID}: "))
            Priority = int(input(f"Enter Priority of {ProcessID}: "))
            IsExecuted = False

            SingleProcessData.extend(
                [ProcessID, ArrivalTime, BurstTime, Priority, IsExecuted, BurstTime]
            )

            AllProcessData.append(SingleProcessData)

        CustomScheduling.SchedulingProcess(
            AllProcessData=AllProcessData, NumProcess=NumProcess
        )

    def SchedulingProcess(self, AllProcessData, NumProcess):
        ExecetionSequence = []


class AutoPriorityScheduling(CustomPriorityScheduling):
    pass


if __name__ == "__main__":
    CustomScheduling = CustomPriorityScheduling()
    AutoScheduling = AutoPriorityScheduling()

    print("Do you want to print documentation?\n[Y/N](Default 'N')\n")
    Decision = input()
    if Decision.lower() == "y":
        print(CustomScheduling.__doc__)
    else:
        pass

    print("Do you want test with custom inputs?\n[Y/N](Default 'N')\n")
    CustomTest = input()
    if CustomTest.lower() == "y":
        print("Enter Number of Process: ")
        NumProcess = int(input())
