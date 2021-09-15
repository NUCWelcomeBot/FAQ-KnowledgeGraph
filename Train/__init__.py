from typing import Dict, List, Tuple

from LAC import LAC

from LoadData import stop_words
from Models.Answer import Answer
from Models.Node import Node

lac = LAC(mode='lac')
objects = []

main_words = ['n', 'nz', 'PER', 'f', 'LOC', 's', 'ORG', 'nw']


def remove_stop_words(sentence: str) -> Tuple[List[str], List[str]]:
    return lac.run(sentence)


def train_data(data: Dict[str, Answer]):
    for question, answer in data.items():
        sentences = remove_stop_words(question)
        node_ege_obj = None
        for j in range(0, len(sentences[0])):
            word = sentences[0][j]
            tag = sentences[1][j]
            if word in stop_words:
                sentences[0].remove(word)
                sentences[1].remove(tag)
            if tag in main_words:
                if node_ege_obj is None:
                    node_ege_obj = Node(word, 'str')
            print(word, tag)
    pass


if __name__ == '__main__':
    train_data({
        '万里长城是中国古代劳动人民血汗的结晶和中国古代文化的象征和中华民族的骄傲': Answer('我爱西樵山')
    })
