from time import sleep, time
from threading import Thread, Lock
from dataclasses import dataclass

"""
In threading, we execute ONE LINE of code at a time but we constantly change which line is run. This is done using 
threading library: we first create some threads, start them and then wait them to finish (using join, for example).
"""

""" BY USING CLASSES

var1 = time()


class MyThread(Thread):
    def __init__(self, text, _time):
        self._text = text
        self._time = _time
        super().__init__()

    def run(self):  # overwrite method super()
        for i in range(2):
            sleep(self._time)
            print(self._text)


t1 = MyThread('Hi! Im thread 1!', 0.25)
t1.start()

t2 = MyThread('Hi! Im thread 2!', 0.10)
t2.start()

t3 = MyThread('Hi! Im thread 3!', 0.05)
t3.start()

print(t2.name)  # Thread-2
print(t2.is_alive())  # return a boolean


# MAIN THREAD
for i in range(10):
    var = time()
    print(i)
    sleep(0.5)

var2 = time()
_time = var2 - var1

print('World')
print(_time)

"""

"""def gonna_take_while(text, _time):
    sleep(_time)
    print(text)


t1 = Thread(target=gonna_take_while, args=('Hello world', 3))
t1.start()

t1 = Thread(target=gonna_take_while, args=('Hello world', 1))
t1.start()

t1 = Thread(target=gonna_take_while, args=('Hello world', 2))
t1.start()

for i in range(10):
    var = time()
    print(i)
    sleep(0.5)"""

"""def gonna_take_while(text, _time):
    sleep(_time)
    print(text)


t1 = Thread(target=gonna_take_while, args=('\n HELLO WORD! \n', 7))
t1.start()
# t1.join() Causes main and secondary current to come together.

while t1.is_alive():
    print('Waiting thread', end='')
    sleep(0.25)
    print('.', end='')
    sleep(0.25)
    print('.', end='')
    sleep(0.25)
    print('.', end='')
    sleep(0.25)
    print('\n')

print('Thread is dead.')"""


@dataclass
class Tickets:
    inventory: int
    lock: Lock = Lock()

    def buy(self, qnt):
        self.lock.acquire()  # Block method by inside,  avoiding
        if self.inventory < qnt:
            self.lock.release()
            print('We no longer have tickets available in sufficient quantity to order.')
            return

        sleep(1)  # Simulating problem with system. All orders receive when stock == 10. But when the system returned,
        # all the backlogs outweighed the total inventory.

        self.inventory -= qnt
        print(f'You bought {qnt} tickets. We still have {self.inventory} in stock.')
        self.lock.release()

    def sell(self):
        pass


if __name__ == '__main__':
    tk = Tickets(10)

    threads = []
    for i in range(1, 10):
        t = Thread(target=tk.buy, args=(i,))
        threads.append(t)

    for thread in threads:
        thread.start()

    executing = True
    while executing:
        executing = False
        for thread in threads:
            if thread.is_alive():
                executing = True
            else:
                executing = False

    print(tk.inventory)
