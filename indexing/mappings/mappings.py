from enum import Enum

from indexing.enums.index_names import IndexName

class ESMappings(dict, Enum):
    UWATERLOO_BM25_INDEX_MAPPING = \
        {
            "settings": {
                "similarity": {
                    "default": {"type": "BM25"}
                }
            },
            "mappings": {
                "properties" : {
                    "courseCode": {"type": "text"},
                    "courseName": {"type": "text"},
                    "courseDescription": {"type": "text"}
                }
            }
        }



    @classmethod
    def get_mapping_from_index_name(cls, index_name: str):
        name_to_mapping = {
            IndexName.UWATERLOO_COURSES_INDEX: cls.UWATERLOO_BM25_INDEX_MAPPING
        }

        return name_to_mapping.get(index_name)