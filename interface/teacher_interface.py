from db import models


def check_course_list_interface(teacher_name):
    # 获取当前老师对象
    teacher_obj = models.Teacher.select(teacher_name)
    # 判断老师对象课程是否有值
    # 老师对象调用查看教授课程方法
    # course_list = teacher_obj.course_list_from_teacher
    course_list = teacher_obj.show_course()
    if course_list:
        return True, course_list
    else:
        return False, "老师没有选择课程！"


def add_course_interface(course_name, teacher_name):
    # 获取当前老师对象
    teacher_obj = models.Teacher.select(teacher_name)
    # 判断当前课程是否在课程列表
    course_list = teacher_obj.course_list_from_teacher
    # 若不存在，则添加
    if course_name in course_list:
        return False, "课程已经存在！"
    teacher_obj.add_course(course_name)
    return True, "添加课程成功"


def get_student_interface(course_name, teacher_name):
    # 获取当前老师对象
    teacher_obj = models.Teacher.select(teacher_name)
    # 获取课程下所有学生
    student_list = teacher_obj.get_student(course_name)
    if not student_list:
        return False, "学生没有选择该课程"
    return True, student_list
