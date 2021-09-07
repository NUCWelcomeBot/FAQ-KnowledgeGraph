from typing import Dict, List

import jieba
import jieba.posseg as pseg
from Models.Answer import Answer
from Models.Question import Question

jieba.enable_parallel(4)


def move_stop_words(sentence: str) -> str:
    sentence = jieba.cut(sentence, cut_all=False)
    return ''.join(sentence)


def train_data(data: Dict[Question, Answer]):
    for question, answer in data.items():
        doc = move_stop_words(question.toString())
        words = pseg.cut(doc)
        for word in words:
            print(word.word, word.flag)
    pass
