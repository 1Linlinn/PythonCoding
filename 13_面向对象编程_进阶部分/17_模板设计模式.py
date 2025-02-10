import time
from abc import ABC, abstractmethod

class JobTemplate(ABC):
    def job(self):
        start = time.time()
        self.task()
        end = time.time()
        print("任务执行时间为：", end - start)

    @abstractmethod
    def task(self):
        pass

class A(JobTemplate):
    def task(self):
        num = 0
        for i in range(1, 800001):
            num += 1

class B(JobTemplate):
    def task(self):
        num = 0
        for i in range(1, 800001):
            num -= 1

if __name__ == "__main__":
    aa = A()
    bb = B()
    aa.job()
    bb.job()

    