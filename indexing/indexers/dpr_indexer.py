from indexing.indexers.indexer import Indexer
from transformers import DPRContextEncoder, DPRContextEncoderTokenizer

class DPRIndexer(Indexer):
    def __init__(self, index_name: str, data: list, tokenizer: str, encoder: str):
        super().__init__(index_name, data)
        self.tokenizer_name = tokenizer
        self.tokenizer = DPRContextEncoderTokenizer.from_pretrained(self.tokenizer_name)
        self.encoder_name = encoder
        self.encoder = DPRContextEncoder.from_pretrained(self.encoder_name)


    def gen_data(self):
        for item in self.data:
            input_ids = self.tokenizer(item["courseDescription"], return_tensors="pt")["input_ids"]
            encoding = self.encoder(input_ids).pooler_output.tolist()[0]
            item["courseDescEncoding"] = encoding
            yield {
                "_index": self.index_name,
                "_source": item
            }
            