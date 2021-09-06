from typing import Dict, List

import jieba as jieba
import spacy

from Models.Answer import Answer
from Models.Question import Question

nlp = spacy.load('en_core_web_sm')


def move_stop_words(sentence: str) -> List[str]:
    sentence = jieba.cut(sentence, cut_all=False)
    return sentence


def train_data(data: Dict[Question, Answer]):
    for question, answer in data.items():

        doc = nlp(question.toString())
        for word in doc:
            print(word)
    pass
