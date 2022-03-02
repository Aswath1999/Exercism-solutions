"""
input_data = ['en', 'circle', 'fold', 'close', 'joy', 'lighten', 'tangle', 'able', 'code', 'culture']
def make_word_groups(vocab_words):
    vocab_words= [vocab_words[0] + x if not x == vocab_words[0] else x for x in vocab_words]
    return ' :: '.join(vocab_words)

print(make_word_groups(input_data))
"""
# input_data = ["heaviness", "sadness", "softness", "crabbiness", "lightness", "artiness", "edginess"]
# input_data=[x[:-4] if not x[-5]=="i" else x[:-5]+"y" for x in input_data]

def noun_to_verb(sentence, index):
    return ((sentence[:-1].split(' ')[index])+'en')

sentence=['asfafsagf afafa.','adgfafa fagfeasf ']
index=[-2,-1]

noun_to_verb(sentence,index)