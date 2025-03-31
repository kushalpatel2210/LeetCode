from threading import Semaphore

class Foo:
    def __init__(self):
        self.first_thread = Semaphore(1)
        self.second_thread = Semaphore(0)
        self.third_thread = Semaphore(0)


    def first(self, printFirst: 'Callable[[], None]') -> None:
        self.first_thread.acquire()
        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        self.second_thread.release()


    def second(self, printSecond: 'Callable[[], None]') -> None:
        self.second_thread.acquire()
        # printSecond() outputs "second". Do not change or remove this line.
        printSecond()
        self.third_thread.release()


    def third(self, printThird: 'Callable[[], None]') -> None:
        self.third_thread.acquire()
        # printThird() outputs "third". Do not change or remove this line.
        printThird()
        self.first_thread.release()