import random

Size = random.randint(1, 51)


def FIFO(Data, Head):

    SeekCount = 0
    Distance, CurrentTrack = 0, 0

    for i in range(Size):
        CurrentTrack = Data[i]

        Distance = abs(CurrentTrack - Head)
        SeekCount += Distance

        Head = CurrentTrack

    print("Total Number of Seek operation: ", SeekCount)

    print("Seek squence: ")
    for i in range(Size):
        print("Position ", i + 1, " : ", Data[i])


if __name__ == "__main__":

    Data = []
    for i in range(Size):
        Temp = random.randint(1, 151)
        Data.append(Temp)

    Head = random.randint(1, 90)

    print("Current Position of Head: ", Head)

    FIFO(Data=Data, Head=Head)
    # print()
