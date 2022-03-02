
def add_prefix_un(word):
    return f'un{word}'


def make_word_groups(vocab_words):
    vocab_words= [vocab_words[0] + x if not x == vocab_words[0] else x for x in vocab_words]
    return ' :: '.join(vocab_words)

def remove_suffix_ness(word):
    word = word[:-4]
    if word[-1] == "i":
      word = word[:-1] + "y"
    return word
    """

    :param word: str of word to remove suffix from.
    :return: str of word with suffix removed & spelling adjusted.

    This function takes in a word and returns the base word with `ness` removed.
    """

    


def noun_to_verb(sentence, index):

    """

    :param sentence: str that uses the word in sentence
    :param index:  index of the word to remove and transform
    :return:  str word that changes the extracted adjective to a verb.

    A function takes a `sentence` using the
    vocabulary word, and the `index` of the word once that sentence
    is split apart.  The function should return the extracted
    adjective as a verb.
    """
    return ((sentence.split(' ')[index])+'en')


def sum(*num):
    count =0 
    for i in num :
       count+=i
    return count

print(sum(5,3))