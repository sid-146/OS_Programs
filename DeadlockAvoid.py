from threading import *
import time

file = "Sudhanwa Kaveeshwar"

s = 1
r = 1
reader_count = 0


def waitc():
    global s
    while s == 0:
        pass
    s = 0


def goc():
    global s
    s = 1


def wait_reader():
    global r
    while r == 0:
        pass
    r = 0


def go_reader():
    global r
    r = 1


def reader(r):

    for i in range(3):
        global reader_count
        wait_reader()

        reader_count = reader_count + 1

        if reader_count == 1:
            waitc()

        go_reader()

        print("reader {0} reading file : {1} ".format(r, file))

        wait_reader()

        reader_count = reader_count - 1
        if reader_count == 0:
            goc()

        go_reader()
        time.sleep(1)


def writer():

    for i in range(2):
        global file
        waitc()
        file = input("write content in file : ")
        print("writer writes : ", file)
        goc()
        time.sleep(1)


writer = Thread(target=writer)
reader1 = Thread(target=reader, args=(1,))
reader2 = Thread(target=reader, args=(2,))
reader1.start()
reader2.start()
writer.start()
