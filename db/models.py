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

    def create_school(self,school_name, school_addr):
        school_obj = School(school_name, school_addr)
        school_obj.save()

    def create_course(self):
        pass

    def create_teacher(self):
        pass


# 学校类
class School(Base):
    def __init__(self, name, addr):
        self.username = name
        self.addr = addr
        self.course_list = []


# 学员类
class Student:
    pass


# 课程类
class Course:
    pass


# 讲师类
class Teacher:
    pass
