from threading import Semaphore

class H2O:
    def __init__(self):
        self.h_sem = Semaphore(2)
        self.o_sem = Semaphore(1)
        self.o_sem.acquire()

    def hydrogen(self, releaseHydrogen: 'Callable[[], None]') -> None:
        self.h_sem.acquire()
        # releaseHydrogen() outputs "H". Do not change or remove this line.
        releaseHydrogen()
        if self.h_sem._value == 0:
            self.o_sem.release()

    def oxygen(self, releaseOxygen: 'Callable[[], None]') -> None:
        self.o_sem.acquire()
        # releaseOxygen() outputs "O". Do not change or remove this line.
        releaseOxygen()        
        if self.h_sem._value == 0:
            self.h_sem.release(2)