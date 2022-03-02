def is_pangram(sentence):
    alphabets="abcdefghijklmnopqrstuvwxyz"
    for i in alphabets:
        if i not in sentence.lower():
            return False
    return True

a="the quick brown fox jumps over the lazy dog"
print(is_pangram(a))
