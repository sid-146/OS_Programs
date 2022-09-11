import random
from tabulate import tabulate


class ProcessNumber:
    """
    generates Random Process Numbers
    """

    # def __inti__(self) -> None:
    #     start = self.start
    #     end = self.end
    #     start = random.randint(1, 10)
    #     end = random.randint(50, 100)

    def getRandomProcessNumber(self):
        # processNumber = random.randint(self.start, self.end)
        start = random.randint(1, 10)
        end = random.randint(50, 100)
        processNumber = random.randint(start, end)
        return processNumber


class showDataFrames:
    """
    Formats DataFrame and print in Table format
    """

    def printDataFrames(DataFrames):
        pass
