import random

# ! This program is made by Sudhanwa Kaveeshwar
#* First come first serve with zero arrival time

def WaitingTimeCal(process, num, BrustTime, WaitingTime):
    WaitingTime[0] = 0

    for _ in range(1, num):
        WaitingTime[_] = BrustTime[_ - 1] + WaitingTime[_ - 1]


def TurnAroundTimeCal(process, num, BrustTime, WaitingTime, TAT):
    for _ in range(num):
        TAT[_] = BrustTime[_] + WaitingTime[_]


def AverageTime(process, num, BrustTime):
    WaitingTime = [0] * num
    Tat = [0] * num
    TotalWT = 0
    TotalTAT = 0

    WaitingTimeCal(process, num, BrustTime, WaitingTime)

    TurnAroundTimeCal(process, num, BrustTime, WaitingTime, Tat)

    for i in range(num):
        TotalWT = TotalWT + WaitingTime[i]
        TotalTAT = TotalTAT + Tat[i]

    print("Avg Waiting Time = ", str(TotalWT / num), " units")
    print("Avg Turn Around time = ", str(TotalTAT / num), " units")


if __name__ == "__main__":
    # num = int(input("Enter number of process : "))
    print("Getting Number of process...")

    num = random.randint(5, 15)
    print("Number of process are: ", num)

    process = [x for x in range(1, num + 1)]
    BurstTime = [random.randint(2, 10) for x in range(1, num + 1)]

    # for i in range(num):
    #     a = int(input("Enter process number: "))
    #     process[i].append(a)
    #     b = input("Enter Burst time of corresponding process: ")
    #     BurstTime[i].append(b)

    process.sort()

    print("Process : BurstTime")
    for i in range(num):
        print(process[i], "\t:\t", BurstTime[i])

    AverageTime(process, num, BurstTime)
    
    print("This program is made by Sudhanwa Kaveehwar") 
    
