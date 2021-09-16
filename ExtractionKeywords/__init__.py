import jieba.analyse
import jieba.posseg as pseg
corpus = '中北大学大数据学院宿舍怎么样'
keywords_tfidf = jieba.analyse.extract_tags(corpus)
print(keywords_tfidf)