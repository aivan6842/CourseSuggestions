from argparse import ArgumentParser
import json

from indexing.enums.index_names import IndexName
from indexing.indexers.index_to_indexer_mapping import INDEX_TO_INDEXER_MAPPING



def index(index_name: str, data: list):
    indexer_class = INDEX_TO_INDEXER_MAPPING.get(index_name)

    indexer = indexer_class(index_name=index_name, data=data)
    print(f"Starting Indexing into {index_name}")
    indexer.index()
    print("Completed Indexing")


if __name__ == "__main__":
    parser = ArgumentParser()

    parser.add_argument("-i", "--index_name",
                        type=str,
                        help="The index name where to store the data",
                        required=True)
    parser.add_argument("-d", "--data_path",
                        type=str,
                        help="Path to JSON file containing data",
                        required=True)

    args = parser.parse_args()

    # get index_name
    index_name = IndexName(args.index_name)

    # load data
    data = []
    with open(args.data_path, "r") as f:
        data = json.load(f)
    
    if not data:
        print("No data")
        exit()

    index(index_name=index_name, data=data)