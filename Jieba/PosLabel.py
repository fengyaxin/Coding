import jieba.posseg as pseg #词性标注

sent = "他在北京大学读书"

words = pseg.cut(sent)
for word, flag in words:
    print("{0} {1}".format(word, flag))