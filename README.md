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

# Scraping
 To run scraper for a website:
  1. Make sure you are in the 'spiders' directory
  2. execute: ``` scrapy runspider $SPIDER_NAME -O $OUTPUT_FILE ```

  example:``` scrapy runspider waterlooCompSci.py -O test.json ```
  
  Note: can pass use paths for the file names
 
# Indexing
Commands to run indexing<br />
BM25 <br />
`python .\indexing\index.py -i uwaterloo-courses -d .\scraping\contents\waterloo\output.json`<br />
DPR <br />
`python .\indexing\index.py -i uwaterloo-courses-dpr -d .\scraping\contents\waterloo\output.json`<br />
T5 <br />
`python .\indexing\index.py -i uwaterloo-courses-t5 -d .\scraping\contents\waterloo\output.json`

# Inference
Commands to run inference
Replace YOUR QUERY with a query string. The RETRIEVERS param can be replaced with any combination of bm25, dpr, or t5. N is the number of returned courses, and the BOOL should be set to true if you would like to rerank the scores. Note reranking automatically occurs if using multiple retrievers.<br />
`python .\inference\infer.py -q "YOUR QUERY" -rt RETRIEVERS -n N -rr BOOL`<br />
As an example of dpr retrieval with reranking<br />
`python .\inference\infer.py -q "Machine Learning" -rt dpr -n 5 -rr True`<br />
As an example BM25 + T5 retrieval (auto reranking)
`python .\inference\infer.py -q "Machine Learning" -rt bm25 t5 -n 5`<br />


# To do
  1. Fine tune DPR
  2. Remove excess info from course descrptions
  3. Investigate low scores 