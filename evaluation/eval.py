from argparse import ArgumentParser

from inference.infer import inference
from evaluation.metrics.mean_reciprocal_rank import MeanReciprocalRank

def evaluate(file: str, retriever_names: list, metric_name: str, rerank: bool = False):
    print(rerank)
    f = open(file, "r")
    row = f.readlines()

    METRIC_MAPPING = {
        "mrr": MeanReciprocalRank
    }

    res = [] #query, y, yhat
    for line in row[1:]:
        line.strip()
        line = line[:-1]
        sep = line.split(",")

        query = sep[0]
        y = [x.replace(" ", "") for x in sep[1:]]
        
        yhat = inference(query=query, retriever_names=retriever_names, rerank=rerank)
        yhat_course_codes = [x[0] for x in yhat]
        res.append((query, y, yhat_course_codes))

    res = res[1:]

    metric = METRIC_MAPPING[metric_name]()
    #print([x[2] for x in res])
    return metric.evaluate(y=[x[1] for x in res], yhat=[x[2] for x in res])



if __name__ == "__main__":
    parser = ArgumentParser()

    parser.add_argument("-f", "--file",
                        type=str,
                        help="Path to file for the test data",
                        required=True)
    parser.add_argument("-rt", "--retrievers",
                        type=str,
                        nargs="*",
                        default=["BM25"],
                        help="list of retrievers",
                        required=True)
    parser.add_argument("-rr", "--rerank",
                        type=bool,
                        default=False,
                        help="Rerank documents using re-ranker. Automatically enabled if more than 1 retriever",
                        required=False)
    parser.add_argument("-m", "--metric",
                        type=str,
                        help="Metric name",
                        required=True)
    
    args = parser.parse_args()

    res = evaluate(file=args.file, 
              retriever_names=args.retrievers, 
              rerank=args.rerank, 
              metric_name=args.metric)
    
    print(res)