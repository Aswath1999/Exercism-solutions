
def find_anagrams(word, candidates):
    return [ana for ana in candidates if sorted(ana.lower())==sorted(word.lower()) and ana.lower()!=word.lower()]

