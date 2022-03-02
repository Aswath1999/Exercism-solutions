class Cipher:
    def __init__(self, key=None):
       self.key=key

    def encode(self, text):
        c=""
        for t in text:
            c+=chr((ord(t)+ord(self.key))%26)
        return c


    def decode(self, text):
        pass
