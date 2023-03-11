from evaluation.metrics.metric import Metric

class MeanReciprocalRank(Metric):
    def evaluate(self, y: list, yhat: list):
        q = len(y)
        res = 0
        for i in range(q):
            top = y[i][0]
            
            index = -1
            try:
                index = yhat[i].index(top)
            except ValueError:
                index = -1   

            recip_rank = 1/index if index != -1 else 0
            res += recip_rank
            
        return res * (1/q) 