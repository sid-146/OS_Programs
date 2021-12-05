import random

# ! This program is made by Sudhanwa Kaveeshwar
# * Shortest Job First


class ShortestJobFirst:
    def TakingData(self, NumProcess):
        AllProcessData = []

        for i in range(NumProcess):

            SingleProcessData = []

            # ProcessID = int(input("Enter Process ID: "))
            # ArrivalTime = int(input(f"Enter Arrival Time for Process {ProcessID}: "))
            # BurstTime = int(input(f"Enter Burst Time for Process {ProcessID}: "))
            # IsExecuted = False

            ProcessID = i + 1
            ArrivalTime = random.randint(1, 51)
            BurstTime = random.randint(1, 151)
            IsExecuted = False

            #! [0:ProcessID, 1:ArrivalTime, 2:BurstTime, 3:IsExecuted]
            SingleProcessData.extend([ProcessID, ArrivalTime, BurstTime, IsExecuted])

            AllProcessData.append(SingleProcessData)

        ShortestJobFirst.schedulingProcess(self, AllProcessData)

    def schedulingProcess(self, AllProcessData):
        StartTime = []
        ExitTime = []
        STime = 0

        # Sort processes according to the Arrival Time
        AllProcessData.sort(key=lambda x: x[1])

        for i in range(len(AllProcessData)):
            ReadyQueue = []
            Temp = []
            NormalQueue = []

            for j in range(len(AllProcessData)):

                #! [0:ProcessID, 1:ArrivalTime, 2:BurstTime, 3:IsExecuted]
                if (AllProcessData[j][1] <= STime) and (AllProcessData[j][3] == False):
                    Temp.extend(
                        [
                            AllProcessData[j][0],
                            AllProcessData[j][1],
                            AllProcessData[j][2],
                        ]
                    )

                    ReadyQueue.append(Temp)
                    Temp = []

                elif AllProcessData[j][3] == False:
                    Temp.extend(
                        [
                            AllProcessData[j][0],
                            AllProcessData[j][1],
                            AllProcessData[j][2],
                        ]
                    )

                    NormalQueue.append(Temp)
                    Temp = []
            #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
            #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
            #! Doone Till HREREERERERRER......................................
            #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
            #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
            #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
            if len(ReadyQueue) != 0:
                # Sort the processes according to the Burst Time
                ReadyQueue.sort(key=lambda x: x[2])

                StartTime.append(STime)
                STime = STime + ReadyQueue[0][2]
                e_time = STime

                ExitTime.append(e_time)

                for k in range(len(AllProcessData)):
                    if AllProcessData[k][0] == ReadyQueue[0][0]:
                        break

                AllProcessData[k][3] = 1
                AllProcessData[k].append(e_time)

            elif len(ReadyQueue) == 0:
                if STime < NormalQueue[0][1]:
                    STime = NormalQueue[0][1]
                StartTime.append(STime)
                STime = STime + NormalQueue[0][2]
                e_time = STime
                ExitTime.append(e_time)
                for k in range(len(AllProcessData)):
                    if AllProcessData[k][0] == NormalQueue[0][0]:
                        break
                AllProcessData[k][3] = 1
                AllProcessData[k].append(e_time)

        t_time = ShortestJobFirst.calculateTurnaroundTime(self, AllProcessData)
        w_time = ShortestJobFirst.calculateWaitingTime(self, AllProcessData)
        ShortestJobFirst.printData(self, AllProcessData, t_time, w_time)

    def calculateTurnaroundTime(self, process_data):
        total_turnaround_time = 0
        for i in range(len(process_data)):
            turnaround_time = process_data[i][4] - process_data[i][1]
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
            waiting_time = process_data[i][5] - process_data[i][2]
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

    def printData(self, process_data, average_turnaround_time, average_waiting_time):
        process_data.sort(key=lambda x: x[0])
        """
        Sort processes according to the Process ID
        """
        print(
            "Process_ID  Arrival_Time  Burst_Time      Completed  Completion_Time  Turnaround_Time  Waiting_Time"
        )

        for i in range(len(process_data)):
            for j in range(len(process_data[i])):

                print(process_data[i][j], end="				")
            print()

        print(f"Average Turnaround Time: {average_turnaround_time}")

        print(f"Average Waiting Time: {average_waiting_time}")


if __name__ == "__main__":
    no_of_processes = int(input("Enter number of processes: "))
    sjf = ShortestJobFirst()
    sjf.TakingData(no_of_processes)
