from threading import Semaphore

class FooBar:
    def __init__(self, n):
        self.n = n
        self.sem_foo = Semaphore(1)
        self.sem_bar = Semaphore(0)
 

    def foo(self, printFoo: 'Callable[[], None]') -> None:
        
        for i in range(self.n):
            self.sem_foo.acquire()
            # printFoo() outputs "foo". Do not change or remove this line.
            printFoo()
            self.sem_bar.release()


    def bar(self, printBar: 'Callable[[], None]') -> None:
        
        for i in range(self.n):
            self.sem_bar.acquire()
            # printBar() outputs "bar". Do not change or remove this line.
            printBar()
            self.sem_foo.release()