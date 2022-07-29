import math
import random

class Class_1():
    def __init__(self, students):
        self.students = students
    
    def pick(self, n):
        self.n = n
        group = random.sample(self.students, n)
        return group
    
    def match_pair(self):
        pair =[]
        if len(self.students)%2:
            pair.append(random.sample(self.students, 3))
        
        for i in self.students:
            for j in pair[0]:
                if i == j:
                    self.students.remove(i)
                else:
                    continue
        for i in self.students:
            pair.append(random.sample(self.students, 2)) 
            print(pair)
            for j in pair:
                if i in j:
                    self.students.remove(i)
                    print(self.students)
    
        return pair

stu_list = Class_1(['김싸피', '최싸피', '정싸피', '천싸피', '유싸피','이싸피','강싸피','손싸피','양싸피'])

#print(stu_list.pick(2))
print(stu_list.match_pair())