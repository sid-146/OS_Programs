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

        while 1:
            ReadyQueue = []
            NormalQueue = []
            TempData = []

            for i in range(len(AllProcessData)):
                # *[ProcessID, ArrivalTime, BurstTime, Priority, IsExecuted, BurstTime]

                # print(STime)
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
                # ? Sorting according to priority
                ReadyQueue.sort(key=lambda x: x[3], reverse=True)

                StartTime.append(STime)
                STime += 1
                ETime = STime

                ExitTime.append(ETime)

                # * Process which are alloted resource are appned in this list
                ExecetionSequence.append(ReadyQueue[0][0])

                for k in range(NumProcess):
                    if AllProcessData[k][0] == ReadyQueue[0][0]:
                        break

                # * reducing burst Time
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
                    STime += 1

                    ETime = STime
                    ExitTime.append(ETime)
                    ExecetionSequence.append(NormalQueue[0][0])

                    for k in range(NumProcess):
                        if AllProcessData[k][0] == NormalQueue[0][0]:
                            break
                    AllProcessData[k][2] = AllProcessData[k][2] - 1

                    if AllProcessData[k][2] == 0:
                        AllProcessData[k][4] = True
                        # *[ProcessID, ArrivalTime, BurstTime, Priority, IsExecuted, BurstTime, ETime]
                        AllProcessData[k].append(ETime)

        AvgTurnAroundTime = CustomScheduling.CalculateTurnAroundTime(
            AllProcessData=AllProcessData, NumProcess=NumProcess
        )

        AvgWaitingTime = CustomScheduling.CalculateWaitingTime(
            AllProcessData=AllProcessData, NumProcess=NumProcess
        )

        CustomScheduling.PrintData(
            AllProcessData=AllProcessData,
            NumProcess=NumProcess,
            AvgTurnAroundTime=AvgTurnAroundTime,
            AvgWaitingTime=AvgWaitingTime,
            ExecutionSequence=ExecetionSequence,
        )

    def CalculateTurnAroundTime(self, AllProcessData, NumProcess):
        # *[ProcessID, ArrivalTime, BurstTime, Priority, IsExecuted, BurstTime, ETime]
        TotalTurnAroundTime = 0

        for i in range(NumProcess):
            TurnAroundTime = AllProcessData[i][6] - AllProcessData[i][1]
            TotalTurnAroundTime += TurnAroundTime

            # *[ProcessID, ArrivalTime, BurstTime, Priority, IsExecuted, BurstTime, ETime, TAT]
            AllProcessData[i].append(TurnAroundTime)

        AvgTurnAroundTime = TotalTurnAroundTime / NumProcess

        return AvgTurnAroundTime

    def CalculateWaitingTime(self, AllProcessData, NumProcess):
        TotalWaitingTime = 0

        for i in range(NumProcess):
            WaitingTime = AllProcessData[i][7] - AllProcessData[i][5]
            TotalWaitingTime += TotalWaitingTime / NumProcess

            # *[ProcessID, ArrivalTime, BurstTime, Priority, IsExecuted, BurstTime, ETime, TAT, WaitingTime]
            AllProcessData[i].append(WaitingTime)

        AvgWaitingTime = TotalWaitingTime / NumProcess

        return AvgWaitingTime

    def PrintData(
        self,
        AllProcessData,
        NumProcess,
        AvgTurnAroundTime,
        AvgWaitingTime,
        ExecutionSequence,
    ):
        # * SingleProcess [ProcessID, ArrivalTime, RemBurstTime, Priority, IsExecuted, BurstTime, ETime, TAT, WaitingTime]
        (
            ProcessID,
            ArrivalTime,
            RemBurstTime,
            Priority,
            IsExecuted,
            BurstTime,
            CompTime,
            TurnAroundTime,
            WaitingTime,
        ) = ([], [], [], [], [], [], [], [], [])

        for i in range(NumProcess):
            ProcessID.append(AllProcessData[i][0])
            ArrivalTime.append(AllProcessData[i][1])
            RemBurstTime.append(AllProcessData[i][2])
            Priority.append(AllProcessData[i][3])
            IsExecuted.append(AllProcessData[i][4])
            BurstTime.append(AllProcessData[i][5])
            CompTime.append(AllProcessData[i][6])
            TurnAroundTime.append(AllProcessData[i][7])
            WaitingTime.append(AllProcessData[i][8])

        print(
            "ProcessID : ArrivalTime :   BurstTime   :    Priority   : CompletionTime : TurnAroundTime : WaitingTime :   IsExecuted"
        )

        for i in range(NumProcess):
            print(
                ProcessID[i],
                "\t:\t",
                ArrivalTime[i],
                "\t:\t",
                BurstTime[i],
                "\t:\t",
                Priority[i],
                "\t:\t",
                CompTime[i],
                "\t:\t",
                TurnAroundTime[i],
                "\t:\t",
                WaitingTime[i],
                "\t:\t",
                IsExecuted[i],
                # "\t:\t",
            )

        print("\nAverage Turn Around Time: ", AvgTurnAroundTime)
        print("\nAverage Waiting Time: ", AvgWaitingTime)
        print("\nExecution Sequence: ", ExecutionSequence)


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

            # *[AutoProcessID,AutoArrivalTime,AutoBurstTime,AutoPriority,IsExecuted,AutoBurstTime]

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
        CustomProcess = input("Custom Process Numbers: (Y/N)? [Default: 'NO']")
        if CustomProcess.lower() == "Y":
            AutoNumProcess = int(input("Enter Number of Process: "))
        else:
            AutoNumProcess = random.randint(1, 31)

        # AutoNumProcess = 15
        print("\nNumber of process are: ", AutoNumProcess)
        AutoScheduling.TakingData(NumProcess=AutoNumProcess)
