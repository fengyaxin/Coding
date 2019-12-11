
import jieba.analyse as anls #关键词提取

'''功能：提取关键词'''

sent = open("all.txt", 'r', encoding='UTF-8').read()

#基于tf-idf提取关键词
print("基于TF-IDF提取关键词结果：")
for x, w in anls.extract_tags(sent, topK=20, withWeight=True):
    print('%s %s' % (x, w))

#基于textrank提取关键词
print("基于textrank提取关键词结果：")
for x, w in anls.textrank(sent, withWeight=True):
    print('%s %s' % (x, w))
