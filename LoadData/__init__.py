from typing import List

source_path = '../DATA/stop_words'
cn_stop_words = f'{source_path}/cn_stopwords.txt'
hit_stop_words = f'{source_path}/hit_stopwords.txt'
scu_stop_words = f'{source_path}/scu_stopwords.txt'
path_list = (cn_stop_words, hit_stop_words, scu_stop_words)
Words = List[str]
stopWords: Words = []


def loadStopWords() -> Words:
    for p in path_list:
        with open(p, 'r') as f:
            words = f.readlines()
            for word in words:
                stopWords.append(word)
    return stopWords