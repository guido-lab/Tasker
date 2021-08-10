import time
from abc import ABC, abstractmethod

class Tasks(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def SumTwoNumbers(num_one, num_two):
        time.sleep(1)
        return num_one + num_two

    @abstractmethod
    def MultipleThreeNumbers(num_one, num_two, num_three):
        return num_one * num_two * num_three
