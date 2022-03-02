drops={'Pling':3,'Plang':5,'Plong':7}

def convert(number):
    sound=''
    for k,v in drops.items():
        if number%v==0:
            sound+=k
    if sound=='':
        return str(number)
    return sound

print(convert(1))