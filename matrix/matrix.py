class Matrix:
    def __init__(self, matrix_string):
        self.m=[[int(i) for i in s.split(" ")]for s in matrix_string.split("\n")]

    def row(self, index):
        return self.m[index-1]

    def column(self, index):
        return [row[index-1]
        for row in self.m]
