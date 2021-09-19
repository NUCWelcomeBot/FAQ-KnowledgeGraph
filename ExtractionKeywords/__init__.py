from typing import List

import jieba.analyse

from LoadData import stop_words
from AIModel import lac

n_word_tag = ['n', 'nz', 'PER', 'LOC', 'ORG', 'TIME', 'nw', 's', 'f']


def get_extraction_keywords(text) -> List[str]:
    results = lac.run(text)
    words = results[0]
    tags = results[1]
    result = []
    for word in words:
        if words in stop_words:
            words.remove(word)
            tags.pop(words.index(word))
    for i in range(len(tags)):
        if tags[i] in n_word_tag:
            if words[i] not in result:
                result.append(words[i])
    return result
