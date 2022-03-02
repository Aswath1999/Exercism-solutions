import re
def is_valid(isbn):
    total=0
    regex_isbn = r"^\d-?\d{3}-?\d{5}-?(X|\d)$"
    if not re.match(regex_isbn,isbn):
        return False
    else:
        isbn=isbn.replace("-","")
        for i in range(10):
            total+=(10-i)*(10 if isbn[i]=="X" else int(isbn[i]))
        return total%11==0

