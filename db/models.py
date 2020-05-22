""""""
from db import db_handler


class Base:
    # 查看数据
    @classmethod
    def select(cls, username):
        obj = db_handler.select_data(cls, username)
        return obj

    # 保存数据
    def save(self):
        # 调用db_handler保存数据
        db_handler.save_data(self)


# 管理员类
class Admin(Base):
    # 调用类的时候触发
    def __init__(self, username, password):
        # 给当前对象赋值
        self.username = username
        self.password = password

    def create_school(self, school_name, school_addr):
        school_obj = School(school_name, school_addr)
        school_obj.save()

    def create_course(self, school_obj, course_name):
        # 调用课程类，实例化创建课程
        course_obj = Course(course_name)
        course_obj.save()
        # 获取当前学校对象，并将课程添加到课程列表中
        school_obj.course_list.append(course_name)
        # 更新学校数据
        school_obj.save()

    def create_teacher(self, teacher_name, teacher_pwd):
        # 调用老师类，实例化得到老师对象
        teacher_obj = Teacher(teacher_name, teacher_pwd)
        teacher_obj.save()


# 学校类
class School(Base):
    def __init__(self, name, addr):
        self.username = name
        self.addr = addr
        self.course_list = []


# 学员类
class Student(Base):
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.course_list = []
        self.score = {}  # {"course_name":0}
        self.payed = {}  # {"course_payed:False}


# 课程类
class Course(Base):
    def __init__(self, course_name):
        self.username = course_name
        self.student_list = []


# 讲师类
class Teacher(Base):
    def __init__(self, teacher_name, teacher_pwd):
        self.username = teacher_name
        self.password = teacher_pwd
        self.course_list_from_teacher = []
