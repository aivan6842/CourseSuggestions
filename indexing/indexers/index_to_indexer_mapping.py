from indexing.enums.index_names import IndexName
from indexing.indexers.bm25_indexer import BM25Indexer
from indexing.indexers.dpr_indexer import DPRIndexer

INDEX_TO_INDEXER_MAPPING = {
    IndexName.UWATERLOO_COURSES_INDEX : BM25Indexer,
    IndexName.UWATERLOO_COURSES_INDEX_DPR: DPRIndexer
}