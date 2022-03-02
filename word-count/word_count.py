from collections import Counter
import re

def count_words(sentence):
   return Counter(re.findall(r"[A-Za-z1-9]+(?:'[a-z]+)?",sentence.lower()))


sentence="Joe can't tell between 'large' and large."
print(re.findall(r"[A-Za-z1-9]+(?:'[a-z]+)?",sentence.lower()))
   
    # counts = dict()
    # words=sentence.maketrans(",_","  ","!!&@$%^&:.")
    # words=sentence.translate(words).lower()
    # words = words.split()        
    # for word in words:       
    #     word=word.strip("\'")       
    #     if word in counts:      
    #         counts[word] += 1
    #     else:  
         
    #         counts[word] = 1
    # return counts
        








# from collections import Counter        
# import re 
# def count_words(phrase):
#     words = re.findall("[a-zA-Z][a-zA-Z']*[a-zA-Z]", phrase.lower())       
#     digits = re.findall("\d", phrase) 
#     return dict(Counter(words + digits))
