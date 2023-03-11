from abc import ABC, abstractmethod

class Metric:
    @abstractmethod
    def evaluate(self, y: list[list], yhat: list[list]):
        raise NotImplementedError