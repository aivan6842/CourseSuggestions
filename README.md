# CourseSuggestions
Suggest Courses from University Based on Interests / Bio


# Parts
  1. Scraping
    - can be avoided if you already have all your schools course data
    - custom for each school
  2. Indexing
    - New index for each school because each school can have different mapping
    - Given json file containing data and a mapping, index into es with correct fields and types
  3. Inference
    - Course suggestions
  4. Evaluation
    - Given "golden dataset" we compare different approaches
 
 
 
 
 # Pipelines
 1. BM25 elastic search default (retrieval + reranking)
 2. DPR (retrieval + reranking)
 3. BM25 (retrieval) + CE (reranking)
 4. DPR (retrieval) + CE (reranking)
 5. DPR + BM25 (retrieval) + CE (reranking)
 
