def is_isogram(string):
    letter=[]
    s=string.lower()
    for c in s:
        if c.isalpha():
            if c in letter:
                return False
            letter.append(c)
    return True

    """from another solution
    
        string = string.lower().replace(' ', '').replace('-', '')
    return len(string) == len(set(string))"""