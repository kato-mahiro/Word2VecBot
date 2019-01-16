#coding:utf-8

from gensim.models import word2vec
model = word2vec.Word2Vec.load("./wiki.model")

def is_exist(keyword):
    try:
        model[keyword]
        return True
    except:
        return False

def posi_posi(posi_list):
    try:
        results = model.wv.most_similar(positive=posi_list)
        synonim = []
        for result in results:
            synonim.append(result[0])
        return(synonim)
    except:
        return False

def posi_nega(posi_list,nega_list):
    try:
        results = model.wv.most_similar(positive=posi_list,negative=nega_list)
        synonim = []
        for result in results:
            synonim.append(result[0])
        return(synonim)
    except:
        return False

while(True):
    posi=input('positive keyword list:')
    posi = posi.split(",")
    nega=input('negative keyword list:')
    nega = nega.split(",")
    print(posi_posi(posi))
    print(posi_nega(posi,nega))
