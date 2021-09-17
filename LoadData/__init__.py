from typing import List

source_path = './DATA/stopwords'
cn_stop_words = f'{source_path}/cn_stopwords.txt'
hit_stop_words = f'{source_path}/hit_stopwords.txt'
scu_stop_words = f'{source_path}/scu_stopwords.txt'
path_list = (cn_stop_words, hit_stop_words, scu_stop_words)
Words = List[str]


def __loadStopWords() -> Words:
    _stop_words: Words = []
    for p in path_list:
        with open(p, 'r', encoding='utf-8') as f:
            words = f.readlines()
            for word in words:
                _stop_words.append(word.replace("\n", ''))
    return _stop_words


stop_words = __loadStopWords()
