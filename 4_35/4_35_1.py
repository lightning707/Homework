from threading import Thread


class Counter(Thread):
    def __init__(self):
        global counter
        global rounds
        counter = 0
        rounds = 100000
        super().__init__()

    def run(self):
        for i in range(rounds):
            global counter
            counter += 1


if __name__ == '__main__':
    th1 = Counter()
    th2 = Counter()

    th1.start()
    th2.start()
    th1.join()
    th2.join()

    print(counter)
