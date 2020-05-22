from db import models


def check_course_list_interface(teacher_name):
    # 获取当前老师对象
    teacher_obj = models.Teacher.select(teacher_name)

    # 判断老师对象课程是否有值
    course_list = teacher_obj.course_list_from_teacher
    if course_list:
        return True, course_list
    else:
        return False, "老师没有选择课程！"
