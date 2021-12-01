import random


class PriorityScheduling:

    """
    * Program for Non preemptive Priority Scheduling for zero arrival Time
    ? Dt 4th september 2021
    ! this program is made by Sudhanwa Kaveeshar
    """

    def TakingData(self, NumProcess):
        # global AllProcessData
        AllProcessData = []
        for i in range(1, NumProcess + 1):
            SingleProcessData = []
            # ProcessID = int(input(f"Enter process ID: "))
            # BurstTime = int(input(f"Enter Burst time of {ProcessID}: "))
            # Priority = int(input(f"Enter Priority of process {ProcessID}: "))

            ProcessID = i
            BurstTime = random.randint(2, 15)
            Priority = random.randint(1, NumProcess + 1)
            SingleProcessData.extend(
                [ProcessID, 0, BurstTime, Priority]  #! arrival time = 0
            )
            AllProcessData.append(SingleProcessData)

        # Schedule.PrintData(AllProcessData, None, None)
        Schedule.SchedulingProcess(AllProcessData=AllProcessData)

    def SchedulingProcess(self, AllProcessData):
        print("Sorting According to priority as Arrival time is zero: ")

        AllProcessData.sort(key=lambda x: x[3], reverse=True)
        StartTime, ExitTime = [], []
        STime = 0

        for i in range(len(AllProcessData)):
            StartTime.append(STime)
            STime += AllProcessData[i][2]
            CompTime = STime
            ExitTime.append(CompTime)

            AllProcessData[i].append(CompTime)

        #! [ProcessID, ArrivalTime , BurstTime, Priority, StartingTime, ExitTime]

        Tat = Schedule.CalTurnAroundTime(AllProcessData=AllProcessData)
        WaitingTime = Schedule.CalWaitingTime(AllProcessData=AllProcessData)

        Schedule.PrintData(AllProcessData, Tat, WaitingTime)

    def CalTurnAroundTime(self, AllProcessData):
        TotalTurnAroundTime = 0
        for i in range(len(AllProcessData)):
            TurnAroundTime = AllProcessData[i][4] - AllProcessData[i][1]
            TotalTurnAroundTime += TurnAroundTime
            AllProcessData[i].append(TurnAroundTime)

            AverageTurnAroundTime = TotalTurnAroundTime / len(AllProcessData)

        return AverageTurnAroundTime

    def CalWaitingTime(self, AllProcessData):
        TotalWaitingTime = 0

        for i in range(len(AllProcessData)):
            WaitingTime = AllProcessData[i][5] - AllProcessData[i][2]
            TotalWaitingTime += WaitingTime
            AllProcessData[i].append(WaitingTime)

        AverageWaitingTime = TotalWaitingTime / len(AllProcessData)

        return AverageWaitingTime

    def PrintData(self, AllProcessData, AvgTAT, AvgWaitingTime):
        (
            ProcessId,
            ArrivalTime,
            BurstTime,
            Priority,
            CompletionTime,
            Tat,
            WaitingTime,
        ) = ([], [], [], [], [], [], [])

        # print("Running printdata")

        # print("Sorting according to ProcessId")
        # AllProcessData.sort(key=lambda x: x[0])

        print("Sorting according to priority")
        AllProcessData.sort(key=lambda x: x[3])

        for i in range(len(AllProcessData)):
            ProcessId.append(AllProcessData[i][0])
            ArrivalTime.append(AllProcessData[i][1])
            BurstTime.append(AllProcessData[i][2])
            Priority.append(AllProcessData[i][3])
            CompletionTime.append(AllProcessData[i][4])
            Tat.append(AllProcessData[i][5])
            WaitingTime.append(AllProcessData[i][6])

        LenJob = len(Priority)

        print(
            "ProcessID : ArrivalTime :   BurstTime   :    Priority   : CompletionTime : TurnAroundTime : WaitingTime "
        )
        for i in range(LenJob):
            print(
                ProcessId[i],
                "\t:\t",
                ArrivalTime[i],
                "\t:\t",
                BurstTime[i],
                "\t:\t",
                Priority[i],
                "\t:\t",
                CompletionTime[i],
                "\t:\t",
                Tat[i],
                "\t:\t",
                WaitingTime[i],
            )

        print("Average Turn Around Time: ", AvgTAT)
        print("Average Waiting Time: ", AvgWaitingTime)


if __name__ == "__main__":
    Schedule = PriorityScheduling()

    Info = Schedule.__doc__
    print(Info)
    # NumProcess = int(input("Enter Number of processes: "))\

    NumProcess = random.randint(1, 30)
    print("Number of precesses are: ", NumProcess)

    Schedule.TakingData(NumProcess)
