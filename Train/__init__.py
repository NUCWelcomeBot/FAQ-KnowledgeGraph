import jiagu
import paddlehub as hub

lac = hub.Module(name="lac")
main_words = ['n', 'nz', 'PER', 'f', 'LOC', 's', 'ORG', 'nw']


# def remove_stop_words(sentence: str) -> Tuple[List[str], List[str]]:
#     return lac.run(sentence)
#
#
# def train_data(data: Dict[str, Answer]):
#     for question, answer in data.items():
#         sentences = remove_stop_words(question)
#         node_ege_obj = None
#         for j in range(0, len(sentences[0])):
#             word = sentences[0][j]
#             tag = sentences[1][j]
#             if word in stop_words:
#                 sentences[0].remove(word)
#                 sentences[1].remove(tag)
#             if tag in main_words:
#                 if node_ege_obj is None:
#                     node_ege_obj = Node(word, 'str')
#             print(word, tag)
#     pass
lac = hub.Module(name="lac")



if __name__ == '__main__':
    text = '洛天依是我老婆'
    results = lac.cut(text=text, use_gpu=False, batch_size=1, return_tag=True)
    print(results)
    words = jiagu.seg(text)
    print(words)
    print(jiagu.pos(words))
    knowledge = jiagu.knowledge(text)
    print(knowledge)