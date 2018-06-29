#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/6/28 0024 22:27
# @Author  : Anthony.Waa
# @Site    : 
# @File    : Oldman.py
# @Software: PyCharm

import os

class School:   # 学校
    def __init__(self,schoool_name,school_address):
        self.school_name = schoool_name
        self.school_address = school_address
        print(schoool_name,school_address)


class Course:   # 课程
    def __init__(self,course_name,course_cycle,course_price,course_area):
        self.course_name = course_name
        self.course_cycle = course_cycle
        self.course_price = course_price
        self.course_area = course_area
        print(course_name,course_cycle,course_price,course_area)

class Classs:   # 班级
    def __init__(self,class_name,class_for_school_area,class_for_course,class_for_teacher):
        self.class_name = class_name
        self.class_for_school_area = class_for_school_area
        self.class_for_course = class_for_course
        self.class_for_teacher = class_for_teacher
        print(class_name,class_for_school_area,class_for_course,class_for_teacher)

class Teacher:  # 教师
    def __init__(self,teacher_name,teacher_for_course,teacher_for_class):
        self.teacher_name = teacher_name
        self.teacher_for_course = teacher_for_course
        self.teacher_for_class = teacher_for_class
        print(teacher_name,teacher_for_course,teacher_for_class)

class Student:  # 学生
    def __init__(self,student_name,student_for_class):
        self.student_name = student_name
        self.student_for_class = student_for_class
        print(student_name,student_for_class)


class Manage:   # 管理员
    def create_school(self):    # 创建学校
        school_name = input('请输入学校名称：').strip()
        school_address = input('请输入学校地址：').strip()
        school = School(school_name,school_address)
        with open('school.txt','a+',encoding='utf-8') as schoolf:
            schoolf.writelines('%s|%s'%(school_name,school_address+ '\n'))
            print('学校信息已录入数据库')



    def create_classs(self):    # 创建班级
        class_name = input('请输入班级名称：').strip()
        class_for_school_area = input('请输入班级所属校区：').strip()
        class_for_course = input('请输入班级所学课程：').strip()
        class_for_teacher = input('请输入班级代课教师：').strip()

        classs = Classs(class_name,class_for_school_area,class_for_course,class_for_teacher)
        with open('class.txt','a+',encoding='utf-8') as classf:
            classf.writelines('%s|%s|%s|%s'%(class_name,class_for_school_area,class_for_course,class_for_teacher+ '\n'))
            print('班级信息已录入数据库')




    def create_course(self):    # 创建课程
        course_name = input('请输入课程名称：').strip()
        course_cycle = input('请输入课程周期(30/365)天：').strip()
        course_price = input('请输入课程价格(300/10000)元：').strip()
        course_area = input('请输入课程所属校区：').strip()
        Course(course_name,course_cycle,course_price,course_area)
        with open('course.txt','a+',encoding='utf-8') as coursef:
            coursef.writelines('%s|%s|%s|%s'%(course_name,course_cycle,course_price,course_area+ '\n'))
            print('课程信息已录入数据库')


    def create_teacher(self):   # 创建教师
        teacher_name = input('请输入教师姓名：').strip()
        teacher_for_course = input('请输入教师所授课程：').strip()
        teacher_for_class = input('请输入教师所教班级：').strip()
        Teacher(teacher_name,teacher_for_course,teacher_for_class)
        with open('teacher.txt', 'a+', encoding='utf-8') as teacherf:
            teacherf.writelines('%s|%s|%s' % (teacher_name, teacher_for_course, teacher_for_class)+ '\n')
            print('教师信息已录入数据库')


    def create_student(self):   # 创建学生
        student_name = input('请输入学生姓名：').strip()
        student_for_class = input('请输入学生所属班级：').strip()
        Student(student_name,student_for_class)
        with open('student.txt', 'a+', encoding='utf-8') as studentf:
            studentf.writelines('%s|%s' % (student_name,student_for_class+ '\n'))
            print('学生信息已录入数据库')



manage = Manage()   # 实例化管理员角色




class Identitys:    # 身份
    def manage_Identitys(self): # 管理员身份
        while True:
            name = input('请输入管理员姓名：').strip()
            passwd = input('请输入管理员密码：').strip()
            with open('manage_identity.txt','r',encoding='utf-8') as manage_readfile:
                for line in manage_readfile:
                    lines = line.split('|')
                    fname = lines[0]
                    fpasswd = lines[1]
                    if name == fname and passwd == fpasswd:
                        print('管理员登录成功')
                        print('''
                            1、创建学校
                            2、创建教室
                            3、创建课程
                            4、创建教师
                            5、创建学生
                        ''')

                        manage_number = {
                            1: manage.create_school,
                            2: manage.create_classs,
                            3: manage.create_course,
                            4: manage.create_teacher,
                            5: manage.create_student
                        }

                        choice_manage_number = input('请输入选项：').strip()
                        if choice_manage_number.isdigit():
                            choice_manage_number = int(choice_manage_number)
                            if 0 < choice_manage_number <= int(choice_manage_number):
                                manage_number[choice_manage_number]()

                            else:
                                print('请重新输入...')
                                continue
                        else:
                            print('请重新输入...')
                            continue




                    user_status['username'] = name
                    user_status['status'] = True
                    return True
                else:
                    manage_readfile.close()
                    with open('manage_identity.txt', 'a+', encoding='utf-8') as manage_writefile:
                        manage_writefile.writelines('%s|%s|%s' % (name, passwd, '管理员'+'\n'))
                        print('用户不存在,已自动注册成功...')
                        print('请重新登陆...')



    def student_Identitys(self):    # 学生身份
        while True:
            name = input('请输入学生姓名：').strip()
            passwd = input('请输入学生密码：').strip()
            with open('student_identity.txt','r',encoding='utf-8') as student_readfile:
                for line in student_readfile:
                    lines = line.split('|')
                    fname = lines[0]
                    fpasswd = lines[1]
                    if name == fname and passwd == fpasswd:
                        print('学生登录成功')

                    with open('course.txt','r',encoding='utf-8') as check_course:
                        for course_line in check_course:
                            course_lines = course_line.split('|')
                        with open('class.txt','r',encoding='utf-8') as check_class:
                            for class_line in check_class:
                                pass



                        user_status['username'] = name
                        user_status['status'] = True
                        return True
                else:
                    student_readfile.close()
                    with open('student_identity.txt', 'a+', encoding='utf-8') as student_writefile:
                        student_writefile.writelines('%s|%s|%s' % (name, passwd, '学生'+'\n'))
                        print('用户不存在,已自动注册成功...')
                        print('请重新登陆...')

    def teacher_Identitys(self):    # 教师身份
        while True:
            name = input('请输入教师姓名：').strip()
            passwd = input('请输入教师密码：').strip()
            with open('teacher_identity.txt','r',encoding='utf-8') as teacher_readfile:
                for line in teacher_readfile:
                    lines = line.split('|')
                    fname = lines[0]
                    fpasswd = lines[1]
                    if name == fname and passwd == fpasswd:
                        print('教师登录成功')
                        user_status['username'] = name
                        user_status['status'] = True
                        return True
                else:
                    teacher_readfile.close()
                    with open('teacher_identity.txt', 'a+', encoding='utf-8') as teacher_readfile:
                        teacher_readfile.writelines('%s|%s|%s' % (name, passwd, '教师'+'\n'))
                        print('用户不存在,已自动注册成功...')
                        print('请重新登陆...')


identitys = Identitys()
user_status = {'username':None,'status':False}

while True:
    print('''
        欢迎来到Oldman教育...
        1、管理员
        2、教师
        3、学生
    ''')

    Identityss_number = {
        1: identitys.manage_Identitys,
        2: identitys.teacher_Identitys,
        3: identitys.student_Identitys
    }

    choice_number = input('请输入选择你的身份：').strip()
    if choice_number.isdigit():
        choice_number = int(choice_number)
        if 0 < choice_number <= int(choice_number):
            Identityss_number[choice_number]()
        else:
            print('请重新输入...')
            continue
    else:
        print('请重新输入...')
        continue


















