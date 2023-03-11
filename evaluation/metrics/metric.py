from abc import ABC, abstractmethod

class Metric:
    @abstractmethod
    def evaluate(self, y: list, yhat: list):
        raise NotImplementedError