import string
import random
class Robot:
    def __init__(self):
        self.name=self.letters_()

    def reset(self):
        self.name=self.letters_()

    def letters_(self):
        random.seed()
        letters="".join(random.choices(string.ascii_uppercase,k=2))
        dig="".join(random.choices(string.digits,k=3))
        return "".join(letters+dig)



