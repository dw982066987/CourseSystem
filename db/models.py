""""""
from db import db_handler


# 管理员类
class Admin:
    # 调用类的时候触发
    def __init__(self, username, password):
        # 给当前对象赋值
        self.username = username
        self.password = password

    # 查看数据
    @classmethod
    def select(cls, username):
        obj = db_handler.select_data(cls, username)
        return obj

    # 保存数据
    def save(self):
        # 调用db_handler保存数据
        db_handler.save_data(self)


# 学校类
class School:
    pass


# 学员类
class Student:
    pass


# 课程类
class Course:
    pass


# 讲师类
class Teacher:
    pass
