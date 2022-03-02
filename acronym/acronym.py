import re
def abbreviate(words):
    pattern=re.findall('[A-Za-z\']+',words)
    return "".join(i[0] for i in pattern).upper()
#     words=words.replace("_","")
#     words=words.replace("-"," ")
#     words=words.split()
#     w=[]
#     for i in words:
#         w.append(i[0])
#     return "".join(w).upper()


# word="The Road _Not_ Taken"
# pattern=re.findall('[A-Za-z\']+',word)
# print("".join(i[0] for i in pattern).upper())