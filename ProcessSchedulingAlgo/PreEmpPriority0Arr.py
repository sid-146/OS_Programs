import random


class CustomPriorityScheduling:
    """
    * This program is made by Sudhanwa Kaveeshwar
    * Program for Preemptive Priority Scheduling with 0 Arrival Time
    ! Info here
    """

    def TakingData(self, NumProcess):
        AllProcessData = []

        for i in range(NumProcess):
            SingleProcessData = []

            ProcessID = int(input("Enter Process ID: "))
            ArrivalTime = 0
            BurstTime = int(input(f"Enter BurstTime of {ProcessID}: "))
            Priority = int(input(f"Enter Priorirty of {ProcessID}: "))
            IsExecuted = False

            # * SingleProcess [ProcessID, ArrivalTime, BurstTime, Priority, IsExecuted, BurstTime]
            #! second bursttime will remain same but first will denote remaning burstTime
            SingleProcessData.extend(
                [ProcessID, ArrivalTime, BurstTime, Priority, IsExecuted, BurstTime]
            )

        AllProcessData.append(SingleProcessData)

        Schedule.SchedulingProcess(AllProcessData, NumProcess)

    def SchedulingProcess(self, AllProcessData, NumProcess: int):
        StartTime = []
        ExitTime = []
        STime = 0

        ExecutionSequence = []

        while True:
            ReadyQueue = []
            TempData = []

            for i in range(NumProcess):
                # * SingleProcess [ProcessID, ArrivalTime, BurstTime, Priority, IsExecuted, BurstTime]
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

            if len(ReadyQueue) == 0:
                break

            if len(ReadyQueue) != 0:
                #! Sorting According to high number high Priority
                ReadyQueue.sort(key=lambda x: x[3], reverse=True)

                StartTime.append(STime)
                STime += 1
                ETime = STime

                ExitTime.append(ETime)

                # * Process which are alloted resource are appned in this list
                ExecutionSequence.append(ReadyQueue[0][0])

                for k in range(NumProcess):
                    if AllProcessData[k][0] == ReadyQueue[0][0]:
                        break

                # * reducing burst Time
                AllProcessData[k][2] = AllProcessData[k][2] - 1

                # * BurstTime 0 then process is terminated
                if AllProcessData[k][2] == 0:
                    AllProcessData[k][4] = True

                    # * SingleProcess [ProcessID, ArrivalTime, BurstTime, Priority, IsExecuted, BurstTime, ETime]
                    AllProcessData[k].append(ETime)

        AvgTurnAroundTime = Schedule.CalculateTurnAroundTime(
            AllProcessData=AllProcessData, NumProcess=NumProcess
        )

        AvgWaitingTime = Schedule.CalculateWaitingTime(
            AllProcessData=AllProcessData, NumProcess=NumProcess
        )

        Schedule.PrintTable(
            AllProcessData=AllProcessData,
            NumProcess=NumProcess,
            AvgTurnAroundTime=AvgTurnAroundTime,
            AvgWaitingTime=AvgWaitingTime,
            ExecutionSequence=ExecutionSequence,
        )

    def CalculateTurnAroundTime(self, AllProcessData, NumProcess: int):
        TotalTurnAroundTime = 0

        for i in range(NumProcess):
            TurnAroundTime = AllProcessData[i][6] - AllProcessData[i][1]
            TotalTurnAroundTime += TurnAroundTime

            # * SingleProcess [ProcessID, ArrivalTime, BurstTime, Priority, IsExecuted, BurstTime, ETime, TAT]
            AllProcessData[i].append(TurnAroundTime)

        AvgTurnAroundTime = TotalTurnAroundTime / NumProcess

        return AvgTurnAroundTime

    def CalculateWaitingTime(self, AllProcessData, NumProcess):
        TotalWaitingTime = 0

        for i in range(NumProcess):
            WaitingTime = AllProcessData[i][7] - AllProcessData[i][5]
            TotalWaitingTime += WaitingTime

            # * SingleProcess [ProcessID, ArrivalTime, BurstTime, Priority, IsExecuted, BurstTime, ETime, TAT, WaitingTime]
            AllProcessData[i].append(WaitingTime)

        AvgWaitingTime = TotalWaitingTime / NumProcess

        return AvgWaitingTime

    def PrintTable(
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
    def TakingData(self, AutoNumProces: int):
        AutoAllProcessData = []

        for i in range(AutoNumProces):
            AutoSingleProcessData = []

            AutoProceesID = i
            AutoArrivalTime = 0
            AutoBurstTime = random.randint(5, AutoNumProces + 1)
            AutoPriority = random.randint(1, AutoNumProces + 1)
            AutoIsExecuted = False

            # ! [AutoProceesID, AutoArrivalTime, AutoBurstTime, AutoPriority, AutoIsExecuted, AutoBurstTime]
            AutoSingleProcessData.extend(
                [
                    AutoProceesID,
                    AutoArrivalTime,
                    AutoBurstTime,
                    AutoPriority,
                    AutoIsExecuted,
                    AutoBurstTime,
                ]
            )

            AutoAllProcessData.append(AutoSingleProcessData)

        CustomPriorityScheduling.SchedulingProcess(
            self, AllProcessData=AutoAllProcessData, NumProcess=AutoNumProcess
        )


if __name__ == "__main__":
    Schedule = CustomPriorityScheduling()
    AutoSchedule = AutoPriorityScheduling()

    print("Do you want to print documentaion")
    decision = input("Enter your decision\n[Y/N] (Default decision is 'NO')\n")

    if decision.lower() == "y":
        print(Schedule.__doc__)
    else:
        pass

    print("Do you want to test with custom inputs? ")
    Custom = input("Enter your decision\n[Y/N] (Default decision is 'NO')\n")

    if Custom.lower() == "y":
        NumProcess = int(input("Enter Number of process: \n"))
        print("Number of Processes are: ", NumProcess, "\n")

        Schedule.TakingData(NumProcess=NumProcess)
    else:
        AutoNumProcess = random.randint(1, 31)
        print("Number of Processes are: ", AutoNumProcess, "\n")

        AutoSchedule.TakingData(AutoNumProcess)
