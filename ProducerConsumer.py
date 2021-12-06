    s = 1
full = 0
empty = 10
i = 0


def wait(s):
    s -= 1
    return s


def signal(s):
    s += 1
    return s


def producer():
    global empty
    global s
    global full
    global i
    empty = wait(empty)
    s = wait(s)
    i += 1
    print("Producer produces the item x")
    s = signal(s)
    full = signal(full)


def consumer():
    global empty
    global s
    global full
    global i
    full = wait(full)
    s = wait(s)
    print("Consumer consumes item x")
    i -= 1
    s = signal(s)
    empty = signal(empty)


if __name__ == "__main__":
    n = 0
    producer()
    consumer()

    print("1.Producer\n2.Consumer\n3.Exit")
    while 1:
        n = int(input("Enter your choice:"))

        if n == 1:
            if s == 1 and empty != 0:
                producer()
            else:
                print("Buffer is full")
        elif n == 2:
            if s == 1 and full != 0:
                consumer()
            else:
                print("Buffer is empty")
        else:
            exit(0)
