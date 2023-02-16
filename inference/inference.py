from argparse import ArgumentParser

from inference.retrievers.bm25_retriever import BM25Retriever
from inference.retrievers.dpr_retriever import DPRRetriever
from inference.retrievers.t5_retriever import T5Retriever
from inference.rerankers.miniLMV2_reranker import MiniLMV2Reranker

def inference(query: str, retrievers: list, k: int = 5, rerank: bool = False) -> list[tuple[str, str, str]]:
    """
    Given a list of retrievers will return top k course suggestions
    Returns : [(course_code, course_name, course_description), ...]
    """

    RETRIEVER_MAP = {
        "bm25" : BM25Retriever,
        "dpr" : DPRRetriever,
        "t5": T5Retriever
    }

    # Init retrievers
    retriever_classes = [RETRIEVER_MAP[retriever.lower()]() for retriever in list(set(retrievers))]

    unranked_res = []
    for retriever in retrievers:
        retrieved_res = retriever.retrieve()
        # unpack es result
        for item in retrieved_res["hits"]["hits"]:
            source_item = item["_source"]
            unranked_res.append((source_item["courseCode"], source_item["courseName"], source_item["courseDescription"]))

    # If only a single retrieved was used, then results are already ranked by es
    # If rerank was enabled for a single retriever, then results are also reranked by reranker
    # If multiple retrievers are used, then all results are ranked by reranker regardless of rerank param
    if len(retriever_classes) > 1:
        rerank = True
    
    reranked_res = unranked_res
    if rerank:
        reranker = MiniLMV2Reranker()
        reranked_res = reranker.rerank(data=unranked_res, query=query)
    
    return reranked_res



if __name__ == "__main__":
    parser = ArgumentParser()

    parser.add_argument("-q", "--query",
                        type=str,
                        help="Query",
                        required=True)
    parser.add_argument("-r", "--retrievers",
                        type=list,
                        nargs="+",
                        default=["BM25"],
                        help="list of retrievers",
                        required=True)
    parser.add_argument("-n", "--num_results",
                        type=int,
                        default=5,
                        help="number of documents retrieved during inference",
                        required=False)
    parser.add_argument("-r", "--rerank",
                        type=bool,
                        default=False,
                        help="Rerank documents using re-ranker. Automatically enabled if more than 1 retriever",
                        required=False)
    
    args = parser.parse_args()

    