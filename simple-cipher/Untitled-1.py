def encode(text,key):
        encrypion=""
        for c in text:
            c=chr((ord(c)+5))
            encrypion=encrypion+c
        return encrypion

text="abc"
key=0
print(encode(text,key))

# print(ord("a"))