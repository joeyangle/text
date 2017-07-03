#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'joeya'
__mtime__ = '2017/4/16'
# code is far away from bugs with the god animal protecting
    I love animals. They taste delicious.
              ┏┓      ┏┓
            ┏┛┻━━━┛┻┓
            ┃      ☃      ┃
            ┃  ┳┛  ┗┳  ┃
            ┃      ┻      ┃
            ┗━┓      ┏━┛
                ┃      ┗━━━┓
                ┃  神兽保佑    ┣┓
                ┃　永无BUG！   ┏┛
                ┗┓┓┏━┳┓┏┛
                  ┃┫┫  ┃┫┫
                  ┗┻┛  ┗┻┛
"""
class School(object):
    def __init__(self,name,addr):
        self.name = name
        self.addr = addr
        self.students = []
        self.teachers = []
        self.staffs = []

    def encoll(self,stu_obj):
        print('为学员%s 办理注册手续'%stu_obj.name)
        self.students.append(stu_obj)

    def hire(self,staff_obj):
        print('雇佣新员工%s' % staff_obj.name)
        self.staffs.append(staff_obj)

class SchoolMember(object):
    def __init__(self,name,age,sex):
        self.name = name
        self.age = age
        self.sex = sex
    def tell(self):
        pass


class Teacher(SchoolMember):
    def __init__(self,name,age,sex,salary,course):
        super(Teacher,self).__init__(name,age,sex)
        self.salary = salary
        self.course = course

    def tell(self):
        print('''
        ---- info of Teacher:%s ----
        Name: %s
        Age:%s
        Sex:%s
        Salary:%s
        Course:%s
        '''%(self.name,self.name,self.age,self.sex,self.salary,self.course))

    def teach(self):
        print('%s is teachiong course [%s]'%(self.name,self.course))

class Student(SchoolMember):
    def __init__(self,name,age,sex,stu_id,grade):
        super(Student,self).__init__(name,age,sex)
        self.stu_id = stu_id
        self.grade = grade


    def tell(self):
        print('''
        ---- info of Student:%s ----
        Name: %s
        Age:%s
        Sex:%s
        Stu_id:%s
        Grade:%s
        '''%(self.name,self.name,self.age,self.sex,self.stu_id,self.grade))

    def pay_tuition(self,amount):
        print('%s has paid tution for $%s'%(self.name,amount))


school = School('老男孩IT','沙河')

t1 = Teacher('Oldboy','56','MF',2000000,'Linux')
t2 = Teacher('Alex','22','M',2000,'PythonDevOps')

s1 = Student('Chen',31,'MF',1001,'PythonDevOps')
s2 = Student('Xu',19,'M',1002,'Linux')

t1.tell()
s1.tell()
school.hire(t1)
school.encoll(s1)
school.encoll(s2)
school.staffs[0].teach()

print(school.students)
print(school.staffs)

for stu in school.students:
    print(stu.pay_tuition(5000))



