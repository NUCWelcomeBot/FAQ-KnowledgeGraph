from typing import List

import jieba.analyse

from LoadData import stop_words
from Train import lac


def get_extraction_keywords(text) -> List[str]:
    results = lac.cut(text=text, use_gpu=False, batch_size=1, return_tag=True)
    for result in results:
        if result in stop_words:
            results.remove(result)
    return results
