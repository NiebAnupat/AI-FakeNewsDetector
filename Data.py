import json
import pandas as pd
from typing import Dict, List
from pythainlp.tokenize import word_tokenize

def __read_jsonlines(file_path: str) -> List[Dict]:
    with open(file_path, 'r', encoding='utf-8') as fp:
        return [json.loads(line) for line in fp.readlines()]

# datasets from https://github.com/byinth/LimeSoda
# Dataset Format
# Each line in the jsonlines file contains:
# Title - a news headline which tokenized by PyICU 2.4.3.
# Detail - a news content which tokenized by PyICU 2.4.3.
# Title Token Tags - a token labels of a news headline (token-level tags).
# Detail Token Tags - a token labels of a news content (token-level tags).
# Document Tag - "Fact News", "Fake News", or "Undefined"


def load_data(file_path: str) -> List[Dict]:
    return __read_jsonlines(file_path)


def tokenizer(text):
    return word_tokenize(text, engine="deepcut")


def preprocess_data(data: str) -> List[str]:
    data = data.replace("\n", "")
    return tokenizer(data)
