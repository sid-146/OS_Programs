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
                # *[ProcessID, ArrivalTime, BurstTime, Priority, IsExecuted, BurstTime]
                [ProcessID, ArrivalTime, BurstTime, Priority, IsExecuted, BurstTime]
            )

            AllProcessData.append(SingleProcessData)

        CustomScheduling.SchedulingProcess(
            AllProcessData=AllProcessData, NumProcess=NumProcess
        )

    def SchedulingProcess(self, AllProcessData, NumProcess):
        StartTime = []
        ExitTime = []
        STime = 0
        ExecetionSequence = []

        # *[ProcessID, ArrivalTime, BurstTime, Priority, IsExecuted, BurstTime]
        # * Sorting according to Arrival Time
        AllProcessData.sort(key=lambda x: x[1])

        while True:
            ReadyQueue = []
            NormalQueue = []
            TempData = []

            for i in range(NumProcess):
                # *[ProcessID, ArrivalTime, BurstTime, Priority, IsExecuted, BurstTime]
                if AllProcessData[i][1] <= STime and AllProcessData[i][4] == False:
                    TempData.extend(
                        [
                            AllProcessData[i][0],
                            AllProcessData[i][1],
                            AllProcessData[i][2],
                            AllProcessData[i][3],
                            AllProcessData[i][5],
                        ]
                    )

                    ReadyQueue.append(TempData)
                    TempData = []

                elif AllProcessData[i][4] == False:
                    TempData.extend(
                        [
                            AllProcessData[i][0],
                            AllProcessData[i][1],
                            AllProcessData[i][2],
                            AllProcessData[i][4],
                            AllProcessData[i][5],
                        ]
                    )

                    NormalQueue.append(TempData)
                    TempData = []

                if len(ReadyQueue) == 0 and len(NormalQueue) == 0:
                    break

                if len(ReadyQueue) != 0:
                    ReadyQueue.sort(key=lambda x: x[3], reverse=True)
                    StartTime.append(STime)
                    STime += STime
                    ETime = STime
                    ExitTime.append(ETime)
                    ExecetionSequence.append(ReadyQueue[0][0])

                    for k in range(NumProcess):
                        if AllProcessData[k][0] == ReadyQueue[0][0]:
                            break
                    AllProcessData[k][2] = AllProcessData[k][2] - 1

                    if AllProcessData[k][2] == 0:
                        #! means process is completed
                        AllProcessData[k][4] = True
                        # *[ProcessID, ArrivalTime, BurstTime, Priority, IsExecuted, BurstTime, ETime]
                        AllProcessData[k].append(ETime)

                if len(ReadyQueue) == 0:
                    NormalQueue.sort(key=lambda x: x[1])
                    if STime < NormalQueue[0][1]:
                        STime = NormalQueue[0][1]
                    StartTime.append(STime)
                    STime = +1
                    ETime = STime
                    ExitTime.appemd(ETime)
                    ExecetionSequence.append(NormalQueue[0][0])

                    for k in range(NumProcess):
                        if AllProcessData[k][0] == NormalQueue[0][0]:
                            break
                    AllProcessData[k][2] = AllProcessData[k][2] - 1

                    if AllProcessData[k][2] == 0:
                        AllProcessData[k][4] = True
                        # *[ProcessID, ArrivalTime, BurstTime, Priority, IsExecuted, BurstTime, ETime]
                        AllProcessData[k].append(ETime)


class AutoPriorityScheduling(CustomPriorityScheduling):
    def TakingData(self, NumProcess: int):
        AutoAllProcessData = []

        for i in range(NumProcess):
            AutoSingleProcessData = []

            AutoProcessID = i + 1
            AutoArrivalTime = random.randint(1, NumProcess + 1)
            AutoBurstTime = random.randint(5, NumProcess + 1)
            AutoPriority = random.randint(1, NumProcess + 1)
            IsExecuted = False

            AutoSingleProcessData.extend(
                [
                    AutoProcessID,
                    AutoArrivalTime,
                    AutoBurstTime,
                    AutoPriority,
                    IsExecuted,
                    AutoBurstTime,
                ]
            )

            AutoAllProcessData.append(AutoSingleProcessData)

        CustomPriorityScheduling.SchedulingProcess(
            self, AllProcessData=AutoAllProcessData, NumProcess=NumProcess
        )


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

        print("\nNumber of process are: ", NumProcess)
        CustomScheduling.TakingData(NumProcess=NumProcess)

    else:
        # AutoNumProcess = random.randint(1, 31)
        AutoNumProcess = 5
        print("\nNumber of process are: ", AutoNumProcess)
        AutoScheduling.TakingData(NumProcess=AutoNumProcess)
