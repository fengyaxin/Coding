import jieba

'''功能：了解jieba分词的3种模式'''


sent = "他来到北京大学读书。"

seg_list1 = jieba.cut(sent, cut_all=True)
print('全模式：', '/'.join(seg_list1))

seg_list2 = jieba.cut(sent, cut_all=False)
print('精确模式：', '/'.join(seg_list2))

seg_list3 = jieba.cut(sent)
print('默认精确模式：', '/'.join(seg_list3))

seg_list4 = jieba.cut_for_search(sent)
print('搜索引擎模式：', '/'.join(seg_list4))
