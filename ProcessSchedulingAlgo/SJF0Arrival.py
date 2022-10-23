import random


# ! This program is made by Sudhanwa Kaveeshwar
# * Shortest Job First


class ShortestJobFirst:
    def TakingData(self, NumProcess: int):
        AllProcessData = []
        self.NumProcess = NumProcess

        for i in range(NumProcess):
            SingleProcessData = []
            #! uncomment for custom inputs
            # ProcessID = int(input(f"Enter process ID: "))
            # BurstTime = int(input(f"Enter Burst time of {ProcessID}: "))
            # ArrivalTime = int(input(f"Enter Priority of process {ProcessID}: "))

            ProcessID = i + 1
            BurstTime = random.randint(1, 50)
            # ArrivalTime = random.randint(0, NumProcess + 1)
            ArrivalTime = 0

            # ArrivalTime = i + 1

            SingleProcessData.extend([ProcessID, ArrivalTime, BurstTime])

            AllProcessData.append(SingleProcessData)
            #! [ProcessID, ArrivalTime, BurstTime]

        ShortestJobFirst.SchedulingProcess(
            self, AllProcessData=AllProcessData, NumProcess=NumProcess
        )

    def SchedulingProcess(self, AllProcessData, NumProcess):
        #! Sorting Accrodring to BurstTime
        AllProcessData.sort(key=lambda x: x[2])

        StartTime = []
        ExitTime = []
        STime = 0

        for i in range(len(AllProcessData)):
            StartTime.append(STime)
            STime = STime + AllProcessData[i][2]
            e_time = STime
            ExitTime.append(e_time)

            #! [ProcessID, ArrivalTime, BurstTime, ExitTime]
            AllProcessData[i].append(e_time)

        AvgTurnAroundTime = ShortestJobFirst.CalTurnAroundTime(self, AllProcessData)

        AvgWaitingTime = ShortestJobFirst.CalWaitingTime(self, AllProcessData)

        ShortestJobFirst.PrintTable(
            self, AllProcessData, AvgTurnAroundTime, AvgWaitingTime, NumProcess
        )

    def CalTurnAroundTime(self, AllProcessData):
        TotalTurnAroundTime = 0
        for i in range(len(AllProcessData)):
            TurnAroundTime = AllProcessData[i][3] - AllProcessData[i][1]

            TotalTurnAroundTime = TotalTurnAroundTime + TurnAroundTime

            #! [ProcessID, ArrivalTime, BurstTime, ExitTime, TurnAroundTime]
            AllProcessData[i].append(TurnAroundTime)

        AvgTurnAroundTime = TotalTurnAroundTime / len(AllProcessData)

        return AvgTurnAroundTime

    def CalWaitingTime(self, AllProcessData):

        TotalWaitingTime = 0

        for i in range(len(AllProcessData)):
            WaitingTime = AllProcessData[i][4] - AllProcessData[i][2]

            TotalWaitingTime = TotalWaitingTime + WaitingTime

            #! [ProcessID, ArrivalTime, BurstTime, ExitTime, TurnAroundTime,WaitingTime]
            AllProcessData[i].append(WaitingTime)

        AvgWaitingTime = TotalWaitingTime / len(AllProcessData)

        return AvgWaitingTime

    def PrintTable(self, AllProcessData, AvgTurnAroundTime, AvgWaitingTime, NumProcess):

        #! [ProcessID, ArrivalTime, BurstTime, ExitTime, TurnAroundTime,WaitingTime]
        (ProcessID, ArrivalTime, BurstTime, CompTime, Tat, WaittingTime) = (
            [],
            [],
            [],
            [],
            [],
            [],
        )

        for i in range(len(AllProcessData)):
            ProcessID.append(AllProcessData[i][0])
            ArrivalTime.append(AllProcessData[i][1])
            BurstTime.append(AllProcessData[i][2])
            CompTime.append(AllProcessData[i][3])
            Tat.append(AllProcessData[i][4])
            WaittingTime.append(AllProcessData[i][5])

        print(
            "ProcessID : BurstTime   :  ArrivalTime   : CompletionTime : TurnAroundTime : WaitingTime"
        )

        for i in range(NumProcess):
            print(
                ProcessID[i],
                "\t:\t",
                BurstTime[i],
                "\t:\t",
                ArrivalTime[i],
                "\t:\t",
                CompTime[i],
                "\t:\t",
                Tat[i],
                "\t:\t",
                WaittingTime[i],
            )

        print("\nAverage Turn Around Time: ", AvgTurnAroundTime, "\n")
        print("Average Waiting Time: ", AvgWaitingTime)


if __name__ == "__main__":

    NumProcess = int(input("Enter number of processes: "))

    sjf = ShortestJobFirst()
    sjf.TakingData(NumProcess)
