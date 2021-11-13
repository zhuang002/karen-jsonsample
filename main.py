import json


class Student:
    def __init__(self, id):
        self.id = id
        self.name = None
        self.age = 0
        self.school = None
        self.grade = 1
        self.gender = 'F'
        self.address = None

    def __str__(self):
        return str(self.id) + "," + str(self.name) + "," + str(self.age) + ", " + str(self.address)


class Address:
    def __init__(self):
        self.street_no = 1
        self.street = "Yong St."
        self.city = "Richmond Hill"
        self.post_code = ""

    def __str__(self):
        return str(self.street_no) + "," + self.street + "," + self.city


student1 = Student(1)
student1.name = 'karen Kwong'
student1.age = 17
student2 = Student(2)
student2.name = 'helen'
student2.age = 16

address1 = Address()
student1.address = address1

student1_dict = student1.__dict__

students = []
with open('data1.json') as f:
    lines = f.readlines()

    for line in lines:
        l = line.rstrip('\n')
        student_json = json.loads(l)
        student = Student(int(student_json['id']))
        student.name = student_json['name']
        student.gender = student_json['gender']
        student.school = student_json['school']
        student.grade = int(student_json['grade'])
        student.age = int(student_json['age'])
        students.append(student)

students.append(student1)




for student in students:
    print(student)

with open('data2.json', 'w+') as wf:
    for student in students:
        wf.write(str(student.__dict__)+'\n')













'''
    {
        'id': 1, 
        'name': 'karen', 
        'age': 17, 
        'school': None, 
        'grade': 1, 
        'gender': 'F', 
        'address': {
            'street_no': 1, 
            'street': 'Yong St.', 
            'city': 'Richmond Hill', 
            'post_code': ''
        }
        
    }
'''
