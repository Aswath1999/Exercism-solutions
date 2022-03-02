student={"Alice":0,"Bob":2,"Charlie":4,"David":6,"Eve":8,"Fred":10,"Ginny":12,
        "Harriet":14,"Ileana":16,"Joseph":18,"Kincaid":20,"Larry":22}
plant={"V":"Violets","R":"Radishes","C":"Clover","G":"Grass"}

class Garden:
    def __init__(self, diagram, students=None):
        self.diagram=diagram
        self.students=students
    def plants(self,name):
        self.name=name
        diagram=self.diagram.split("\n")
        v=[]
        if self.name not in student:
            self.students=sorted(self.students)
            for i in diagram:
                v.extend([plant[i[(self.students.index(self.name))*2]],plant[i[(self.students.index(self.name)*2)+1]]])
            return v
        else:
            for i in diagram:
                v.extend([plant[i[student[self.name]]],plant[i[student[self.name]+1]]])
            return v



students=["Samantha", "Patricia", "Xander", "Roger"]
Plants="VCRRGVRG\nRVGCCGCV"
students=sorted(students)
Plants=Plants.split("\n")
name="Patricia"
print(students.index(name))
v=[]
for i in Plants:
    v.extend([plant[i[students.index(name)*2]],plant[i[(students.index(name))*2+1]]])
print(v)

    
