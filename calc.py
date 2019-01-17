#coding:utf-8

from gensim.models import word2vec
from parsing import parsing
model = word2vec.Word2Vec.load("./wiki.model")

def is_exist(keyword):
    try:
        model[keyword]
        return True
    except:
        return False

def exist(wordlist):
    del_key = []

    for i in range(len(wordlist)):
        if is_exist(wordlist[i]):
            pass
        else:
            del_key.append(i)

    for i in del_key:
        del(wordlist[i])

    return wordlist


def posi_posi(posi_list):
    try:
        results = model.wv.most_similar(positive=posi_list)
        synonim = []
        for result in results:
            synonim.append(result[0])
        return(synonim)
    except:
        return False

def nega_nega(nega_list):
    try:
        results = model.wv.most_similar(negative=nega_list)
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
    string=input('計算式:')
    posi_list,nega_list = parsing(string)
    posi_list=exist(posi_list)
    nega_list=exist(nega_list)

    if(len(posi_list)==0):
        print(nega_nega(nega_list))
    elif(len(nega_list)==0):
        print(posi_posi(posi_list))
    else:
        print(posi_nega(posi_list,nega_list))

    print("---")
