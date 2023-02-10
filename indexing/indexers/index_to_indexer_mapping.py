from indexing.enums.index_names import IndexName
from indexing.indexers.bm25_indexer import BM25Indexer

INDEX_TO_INDEXER_MAPPING = {
    IndexName.UWATERLOO_COURSES_INDEX : BM25Indexer
}