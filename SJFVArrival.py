import random

#! Program created and managed by Sudhanwa Kaveeshwar
#! Short Job First with different Arrival Time


class SJF:
    def TakingData(self, NumProcess):
        AllProcessData = []

        for i in range(NumProcess):
            SingleProcessData = []
            # ProcessID = int(input("Enter Process ID: "))
            # ArrivalTime = int(input(f"Enter Arrival Time for Process {ProcessID}: "))
            # BurstTime = int(input(f"Enter Burst Time for Process {ProcessID}: "))
            # IsExecuted = False

            ProcessID = i + 1
            ArrivalTime = random.randint(1, 29)
            BurstTime = random.randint(1, 99)
            IsExecuted = False

            SingleProcessData.extend(
                [ProcessID, ArrivalTime, BurstTime, IsExecuted, BurstTime]
            )

            AllProcessData.append(SingleProcessData)

        SJF.SchedulingProcess(self, AllProcessData)

    def SchedulingProcess(self, AllProcessData):
        StartTime = []
        ExitTime = []
        STime = 0

        ProcessingSequence = []

        # Sort processes according to the Arrival Time
        #! [ProcessID, ArrivalTime, BurstTime, IsExecuted, BurstTime]
        AllProcessData.sort(key=lambda x: x[1])

        while True:
            ReadyQueue = []
            NormalQueue = []
            Temp = []

            for i in range(len(AllProcessData)):

                #! [ProcessID, ArrivalTime, BurstTime, IsExecuted, BurstTime]
                if AllProcessData[i][1] <= STime and AllProcessData[i][3] == 0:
                    Temp.extend(
                        [
                            AllProcessData[i][0],
                            AllProcessData[i][1],
                            AllProcessData[i][2],
                            AllProcessData[i][4],
                        ]
                    )
                    ReadyQueue.append(Temp)
                    Temp = []

                elif AllProcessData[i][3] == 0:
                    Temp.extend(
                        [
                            AllProcessData[i][0],
                            AllProcessData[i][1],
                            AllProcessData[i][2],
                            AllProcessData[i][4],
                        ]
                    )
                    NormalQueue.append(Temp)
                    Temp = []

            if len(ReadyQueue) == 0 and len(NormalQueue) == 0:
                break

            #! [ProcessID, ArrivalTime, BurstTime, IsExecuted, BurstTime]
            if len(ReadyQueue) != 0:
                # Sort processes according to Burst Time
                ReadyQueue.sort(key=lambda x: x[2])

                StartTime.append(STime)
                STime = STime + 1
                ETime = STime

                ExitTime.append(ETime)
                ProcessingSequence.append(ReadyQueue[0][0])

                for k in range(len(AllProcessData)):
                    if AllProcessData[k][0] == ReadyQueue[0][0]:
                        break

                AllProcessData[k][2] = AllProcessData[k][2] - 1

                # If Burst Time of a process is 0, it means the process is completed
                if AllProcessData[k][2] == 0:
                    AllProcessData[k][3] = 1
                    AllProcessData[k].append(ETime)

            if len(ReadyQueue) == 0:
                if STime < NormalQueue[0][1]:
                    STime = NormalQueue[0][1]

                StartTime.append(STime)
                STime = STime + 1
                ETime = STime
                ExitTime.append(ETime)

                ProcessingSequence.append(NormalQueue[0][0])

                for k in range(len(AllProcessData)):
                    if AllProcessData[k][0] == NormalQueue[0][0]:
                        break

                AllProcessData[k][2] = AllProcessData[k][2] - 1

                # If Burst Time of a process is 0, it means the process is completed
                if AllProcessData[k][2] == 0:
                    AllProcessData[k][3] = 1
                    AllProcessData[k].append(ETime)

        t_time = SJF.calculateTurnaroundTime(self, AllProcessData)
        w_time = SJF.calculateWaitingTime(self, AllProcessData)

        SJF.printData(self, AllProcessData, t_time, w_time, ProcessingSequence)

    def calculateTurnaroundTime(self, process_data):
        total_turnaround_time = 0
        for i in range(len(process_data)):
            turnaround_time = process_data[i][5] - process_data[i][1]
            """
            turnaround_time = completion_time - arrival_time
            """
            total_turnaround_time = total_turnaround_time + turnaround_time
            process_data[i].append(turnaround_time)
        average_turnaround_time = total_turnaround_time / len(process_data)
        """
        average_turnaround_time = total_turnaround_time / no_of_processes
        """
        return average_turnaround_time

    def calculateWaitingTime(self, process_data):
        total_waiting_time = 0
        for i in range(len(process_data)):
            waiting_time = process_data[i][6] - process_data[i][4]
            """
            waiting_time = turnaround_time - burst_time
            """
            total_waiting_time = total_waiting_time + waiting_time
            process_data[i].append(waiting_time)
        average_waiting_time = total_waiting_time / len(process_data)
        """
        average_waiting_time = total_waiting_time / no_of_processes
        """
        return average_waiting_time

    def printData(
        self,
        process_data,
        average_turnaround_time,
        average_waiting_time,
        sequence_of_process,
    ):
        process_data.sort(key=lambda x: x[0])
        """
        Sort processes according to the Process ID
        """
        print(
            "Process_ID  Arrival_Time  Rem_Burst_Time      Completed  Orig_Burst_Time Completion_Time  Turnaround_Time  Waiting_Time"
        )
        for i in range(len(process_data)):
            for j in range(len(process_data[i])):
                print(process_data[i][j], end="\t\t")
            print()
        print(f"Average Turnaround Time: {average_turnaround_time}")
        print(f"Average Waiting Time: {average_waiting_time}")
        # print(f"Sequence of Process: {sequence_of_process}")


if __name__ == "__main__":
    no_of_processes = int(input("Enter number of processes: "))
    sjf = SJF()
    sjf.TakingData(no_of_processes)
