import jieba

'''功能：添加用户自定义词典'''

sent = "周大福是创新办主任也是云计算方面的专家"

seg_list = jieba.cut(sent, cut_all=False)
print('未添加用户词典：', '/'.join(seg_list))

#加载用户自定义词典
jieba.load_userdict("userDic.txt")

seg_list = jieba.cut(sent, cut_all=False)
print('添加用户词典：', '/'.join(seg_list))