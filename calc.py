#coding:utf-8

from gensim.models import word2vec
model = word2vec.Word2Vec.load("./wiki.model")

def getvec(keyword):
    """
    引数の単語のベクトルを返す関数
    """
    try:
        return(model[keyword])
    except:
        return False

while(True):
    word = input('キーワードを入力:')
    word = str(word)
    print(getvec(word))
