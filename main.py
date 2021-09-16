# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.



# Press the green button in the gutter to run the script.
import jiagu

from ExtractionKeywords import get_extraction_keywords

if __name__ == '__main__':
    text = '洛天依是我老婆'
    get_extraction_keywords(text)
    words = jiagu.seg(text)
    print(words)
    print(jiagu.pos(words))
    knowledge = jiagu.knowledge(text)
    print(knowledge)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
