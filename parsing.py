#coding:utf-8
import re
import sys
args = sys.argv

string = args[1] #引数にとった文字列
if string[0] != '+' and string[0] != '-':
    string='+' + string


posilist=['']
posi_n = 0
negalist=['']
nega_n = 0

for i in string:
    if i == '+':
        posilist.append('')
        posi_n += 1
        flag = 'p'
    elif i == '-':
        negalist.append('')
        nega_n += 1
        flag = 'n'
    else:
        if flag == 'p':
            posilist[posi_n -1] += i
        elif flag == 'n':
            negalist[nega_n -1] += i

posilist=posilist[:-1]
negalist=negalist[:-1]

print("posilist:",posilist)
print("negalist:",negalist)
