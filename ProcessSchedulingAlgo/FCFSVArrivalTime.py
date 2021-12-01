import random

# * Program for first come first serve with variable arrival time
# ! This program is made by Sudhanwa Kaveeshwar
# ? Dt. 31 August 2021


class FCFS:
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
            ArrivalTime = random.randint(0, NumProcess + 1)
            # ArrivalTime = i + 1

            SingleProcessData.extend([ProcessID, BurstTime, ArrivalTime])

            AllProcessData.append(SingleProcessData)
            #! [ProcessID, BurstTime, ArrivalTime]

        FCFS.SchedulingProcess(
            self, AllProcessData=AllProcessData, NumProcess=NumProcess
        )

    def SchedulingProcess(self, AllProcessData, NumProcess):

        #! [ProcessID, BurstTime, ArrivalTime, ExitTime]
        # ? sorting according to Arrival time
        AllProcessData.sort(key=lambda x: x[2])
        StartTime, ExitTime = [], []
        STime = 0

        for i in range(len(AllProcessData)):
            if STime < AllProcessData[i][2]:
                STime = AllProcessData[i][2]

            StartTime.append(STime)
            STime += AllProcessData[i][1]
            CompTime = STime
            ExitTime.append(CompTime)
            AllProcessData[i].append(CompTime)

        # print("EXITTIME: ", ExitTime)
        # print("StartTime: ", StartTime)

        AvgTurnAroundTime = FCFS.CalTurnAroundTime(self, AllProcessData=AllProcessData)
        AvgWaitingTime = FCFS.CalWaitingTime(self, AllProcessData=AllProcessData)

        FCFS.PrintTable(
            self,
            AllProcessData=AllProcessData,
            AvgTurnAroundTime=AvgTurnAroundTime,
            AvgWaitingTime=AvgWaitingTime,
            NumProcess=NumProcess,
        )

    def CalTurnAroundTime(self, AllProcessData):
        #! [ProcessID, BurstTime, ArrivalTime, ExitTime, TurnAroundTime]
        TotalTurnAroundTime = 0

        for i in range(len(AllProcessData)):
            TurnAroundTime = AllProcessData[i][3] - AllProcessData[i][2]
            # * completiontime - Arrival time
            TotalTurnAroundTime += TurnAroundTime

            AllProcessData[i].append(TurnAroundTime)

        AvgTurnAroundTime = TotalTurnAroundTime / len(AllProcessData)

        return AvgTurnAroundTime

    def CalWaitingTime(self, AllProcessData):
        #! [ProcessID, BurstTime, ArrivalTime, ExitTime, TurnAroundTime, WaitingTime]
        TotalWaitingTime = 0

        for i in range(len(AllProcessData)):
            Waitingtime = AllProcessData[i][4] - AllProcessData[i][1]
            # * turnaroundtime - bursttime

            AllProcessData[i].append(Waitingtime)

            TotalWaitingTime += Waitingtime

        AvgWaitingTime = TotalWaitingTime / len(AllProcessData)

        return AvgWaitingTime

    def PrintTable(self, AllProcessData, AvgTurnAroundTime, AvgWaitingTime, NumProcess):
        (ProcessID, BurstTime, ArrivalTime, CompTime, Tat, WaittingTime) = (
            [],
            [],
            [],
            [],
            [],
            [],
        )
        # print("Sorting According to ProcessID\n\n")
        # AllProcessData.sort(key=lambda x: x[0])

        # print("Sorting According to Arrival Time\n\n")
        # AllProcessData.sort(key=lambda x: x[2])

        for i in range(len(AllProcessData)):
            ProcessID.append(AllProcessData[i][0])
            BurstTime.append(AllProcessData[i][1])
            ArrivalTime.append(AllProcessData[i][2])
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

        print("Average Turn Around Time: ", AvgTurnAroundTime, "\n")
        print("Average Waiting Time: ", AvgWaitingTime)


if __name__ == "__main__":
    fcfs = FCFS()

    print("Program made by Sudhanwa Kaveeshwar \n")
    print("First Come First server for variable arrival time\n")
    # NumProcess = int(input("Enter the number of process: "))
    NumProcess = random.randint(1, 30)
    print("The number of processes are: ", NumProcess)
    fcfs.TakingData(NumProcess=NumProcess)
