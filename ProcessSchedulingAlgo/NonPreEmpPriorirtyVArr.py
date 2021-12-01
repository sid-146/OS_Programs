import random


class PriorityScheduling:

    """
    * program for Non preemptive Variable Arrival time for Priority Scheduling
    ! 4th septmber 2021
    ! this program is made by Sudhanwa Kaveeshwar
    """

    def TakingData(self, NumProcess):
        self.NumProcess = NumProcess

        AllProcessData = []

        for i in range(1, NumProcess + 1):
            SingleProcessData = []
            # ProcessID = int(input(f"Enter process ID: "))
            # BurstTime = int(input(f"Enter Burst time of {ProcessID}: "))
            # ArrivalTime = int(input(f"Enter arrival time of {ProcessID}: "))
            # Priority = int(input(f"Enter Priority of process {ProcessID}: "))

            ProcessID = i
            ArrivalTime = 0 + i - 1
            # ArrivalTime = random.randint(0, NumProcess + 1)
            BurstTime = random.randint(1, 41)
            Priority = random.randint(1, 41)

            #! IsExecuted denotes the state of process
            # *True mean execution is complete and vice versa
            IsExecuted = False  # default is False

            # * [ProcessID, ArrivalTime, BurstTime, Priority, IsExecuted]

            SingleProcessData.extend(
                [ProcessID, ArrivalTime, BurstTime, Priority, IsExecuted]
            )

            AllProcessData.append(SingleProcessData)

        # for i in range(len(AllProcessData)):
        #     print(AllProcessData[i])

        Scheduling.SchedulingProcess(AllProcessData=AllProcessData)

    def SchedulingProcess(self, AllProcessData: list):
        # * [ProcessID, ArrivalTime, BurstTime, Priority, IsExecuted]

        StartTime, ExitTime = [], []
        STime = 0

        # * Sorting According to Arrival Time
        AllProcessData.sort(key=lambda x: x[1])

        for i in range(len(AllProcessData)):
            # print(AllProcessData[i], "I loop")

            ReadyQueue, NormalQueue, TempHold = ([], [], [])

            for j in range(len(AllProcessData)):
                # print(AllProcessData[j], "j loop")

                #! checking if AT is smaller than starttime of process and in not terminated yet
                if (AllProcessData[j][1] <= STime) and (AllProcessData[j][4] == False):
                    # print(STime, "STime")

                    # * [ProcessID, ArrivalTime, BurstTime, Priority, IsExecuted]
                    TempHold.extend(
                        [
                            AllProcessData[j][0],
                            AllProcessData[j][1],
                            AllProcessData[j][2],
                            AllProcessData[j][3],
                        ]
                    )

                    ReadyQueue.append(TempHold)
                    TempHold = []

                elif AllProcessData[j][4] == False:
                    TempHold.extend(
                        [
                            AllProcessData[j][0],
                            AllProcessData[j][1],
                            AllProcessData[j][2],
                            AllProcessData[j][3],
                        ]
                    )

                    NormalQueue.append(TempHold)
                    TempHold = []

            if len(ReadyQueue) != 0:
                # * Sorting according priority; Higher value higher priority

                # * [ProcessID, ArrivalTime, BurstTime, Priority, IsExecuted]
                ReadyQueue.sort(key=lambda x: x[3], reverse=True)

                # print("Len RQ", len(ReadyQueue), "Sorted RQ", ReadyQueue)

                StartTime.append(STime)
                STime += ReadyQueue[0][2]
                ETime = STime
                ExitTime.append(ETime)

                for k in range(len(AllProcessData)):

                    if AllProcessData[k][0] == ReadyQueue[0][0]:
                        #! will run until ProcessID match is not found
                        break

                AllProcessData[k][4] = True
                AllProcessData[k].append(ETime)

                # print(AllProcessData)

            elif len(ReadyQueue) == 0:
                # print("running len == 0")
                if STime < NormalQueue[0][1]:
                    STime = NormalQueue[0][1]

                StartTime.append(STime)
                STime += NormalQueue[0][2]
                ETime = STime

                ExitTime.append(ETime)

                for k in range(len(AllProcessData)):
                    if AllProcessData[k][0] == NormalQueue[0][0]:
                        break

                    AllProcessData[k][4] = True
                    AllProcessData[k].append(ETime)

        AvgTurnAroundTime = Scheduling.CalculateTrunAroundTime(
            AllProcessData=AllProcessData, NumProcess=NumProcess
        )

        AvgWaitingTime = Scheduling.CalculateWaitingTime(
            AllProcessData=AllProcessData, NumProcess=NumProcess
        )

        Scheduling.PrintTable(
            AllProcessData=AllProcessData,
            NumProcess=NumProcess,
            AvgTurnAroundTime=AvgTurnAroundTime,
            AvgWaitingTime=AvgWaitingTime,
        )

    def CalculateTrunAroundTime(self, AllProcessData, NumProcess):
        TotalTurnAroundTime = 0

        # * [ProcessID, ArrivalTime, BurstTime, Priority, IsExecuted, Termination]
        for i in range(len(AllProcessData)):
            #     print(AllProcessData[i])

            TurnAroundTime = AllProcessData[i][5] - AllProcessData[i][1]
            #! Completion Time - ArrivalTime

            TotalTurnAroundTime += TurnAroundTime
            AllProcessData[i].append(TurnAroundTime)

        # * [ProcessID, ArrivalTime, BurstTime, Priority, IsExecuted, CompletionTime,TAT]

        AvgTotalTurnAroundTime = TotalTurnAroundTime / NumProcess

        return AvgTotalTurnAroundTime

    def CalculateWaitingTime(self, AllProcessData, NumProcess):
        TotalWaitingTime = 0

        for i in range(NumProcess):
            WaitingTime = AllProcessData[i][6] - AllProcessData[i][2]
            #! TurnAroundTime - BurstTime

            TotalWaitingTime += WaitingTime
            AllProcessData[i].append(WaitingTime)
            # print(i, AllProcessData[i])

        # * [ProcessID, ArrivalTime, BurstTime, Priority, IsExecuted, CompletionTime,TAT, WaitingTime]
        AvgWaitingTime = TotalWaitingTime / NumProcess

        return AvgWaitingTime

    def PrintTable(
        self, AllProcessData, NumProcess: int, AvgTurnAroundTime, AvgWaitingTime
    ):
        # * [ProcessID, ArrivalTime, BurstTime, Priority, IsExecuted, CompletionTime,TAT, WaitingTime] index 0 to 7
        (
            ProcessID,
            ArrivalTime,
            BurstTime,
            Priority,
            IsExecuted,
            CompletionTime,
            TurnAroundTime,
            WaitingTime,
        ) = ([], [], [], [], [], [], [], [])

        print(
            "ProcessID : ArrivalTime :   BurstTime   :    Priority   : CompletionTime : TurnAroundTime : WaitingTime :   IsExecuted"
        )

        # * [ProcessID, ArrivalTime, BurstTime, Priority, IsExecuted, CompletionTime,TAT, WaitingTime] index 0 to 7
        for i in range(NumProcess):
            ProcessID.append(AllProcessData[i][0])
            ArrivalTime.append(AllProcessData[i][1])
            BurstTime.append(AllProcessData[i][2])
            Priority.append(AllProcessData[i][3])
            IsExecuted.append(AllProcessData[i][4])
            CompletionTime.append(AllProcessData[i][5])
            TurnAroundTime.append(AllProcessData[i][6])
            WaitingTime.append(AllProcessData[i][7])

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
                CompletionTime[i],
                "\t:\t",
                TurnAroundTime[i],
                "\t:\t",
                WaitingTime[i],
                "\t:\t",
                IsExecuted[i],
            )

        print(f"Average TurnAroundTime: {AvgTurnAroundTime}\n")
        print(f"Average Waiting Time: {AvgWaitingTime}\n")


if __name__ == "__main__":
    Scheduling = PriorityScheduling()

    Info = Scheduling.__doc__
    print(Info, "\n")

    NumProcess = random.randint(1, 31)
    # NumProcess = int(input("Enter Number of Process"))
    print("Number of process are: ", NumProcess)

    Scheduling.TakingData(NumProcess=NumProcess)
