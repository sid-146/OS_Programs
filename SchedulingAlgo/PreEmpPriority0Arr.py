import random


class PriorityScheduling:
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


if __name__ == "__main__":
    print("Do you want to print documentaion")
