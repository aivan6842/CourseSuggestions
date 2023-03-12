from evaluation.metrics.metric import Metric
from sklearn.metrics import recall_score
from sklearn.preprocessing import MultiLabelBinarizer

class Recall(Metric):
    def evaluate(self, y: list, yhat: list):
        sum = 0
        for i in range(len(y)):
            try:
                sum += recall_score(y[i], yhat[i], average='macro')
            except ValueError:
               print(y[i])
               print(yhat[i])
           
        
        return sum/len(y)
        #for i in range(len(y)):
            #print(f"y: {y[i]}, yhat: {yhat[i]}")
        
        #yhat = MultiLabelBinarizer().fit_transform(yhat)
        #return recall_score(y, yhat, average='macro')