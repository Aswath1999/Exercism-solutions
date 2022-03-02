class School:
    def __init__(self):
        self.n=[]
        self.g=[]

    def add_student(self, name, grade):
        self.name=name
        self.n.append(self.name)
        self.g.append(grade)

    def roster(self):
        ros=dict(zip(self.n,self.g))
        names=dict(sorted(ros.items(),key=lambda item:item[0]))
        names=dict(sorted(names.items(),key=lambda item:item[1]))
        return list(names.keys())

    def grade(self, grade_number):
        self.grade_number=grade_number
        ros=dict(zip(self.n,self.g))
        names=dict(sorted(ros.items(),key=lambda item:item[0]))
        return [k for k,v in names.items() if v==grade_number]

