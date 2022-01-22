#input_str = "Hello; welcome, to the world of micro-services."
#output_str = "olleH; emoclew, ot eht dlrow fo seciv-resorcim."

import re
#input_str = "Hello; welcome, to the world of micro-services."
input_str = "micro-services."

#"h".isalpha()
'''
input_str_list=input_str.split(" ")

for i in input_str_list:
    rev = []
    for j in i:
        if str(j).isalpha():
            rev=j+rev
            #print(rev)
        else:
            index=i.index(j)
            indexList.append(j)
            print(index)
            rev = j+rev
    #print(rev)
    break


for i in input_str_list:
    spChar=""
    if re.findall('\W+',i)[0]:
        spChar=re.findall('\w+',i)[0]
        i
    revString=b[::-1]+spChar
    revString=revString+i[::-1]+" "

print(revString)
'''



import requests

#a=requests.get("http://natas0.natas.labs.overthewire.org/" params{username:"",password:""} )
a=requests.get("http://natas0.natas.labs.overthewire.org/")

print(a.text)



