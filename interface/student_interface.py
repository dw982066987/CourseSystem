from db import models


def student_register_interface(username, password):
    student_obj = models.Student.select(username)
    if student_obj:
        return False, "学生用户已存在！"
    student_obj = models.Student(username, password)
    student_obj.save()
    return True, "注册成功！"


# def student_login_interface(username, password):
#     student_obj = models.Student.select(username)
#     if not student_obj:
#         return False, "学生用户不存在，请重新输入！"
#     if password == student_obj.password:
#         return True, "登陆成功！"
#     else:
#         return False, "密码错误，请重新输入！"

def add_school_interface(school_name, student_name):
    student_obj = models.Student.select(student_name)
    if student_obj.school:
        return False, "当前学生已经选择学校!"
    # 若不存在学校,则给调用学生对象中选择学校的方法,实现学生添加学校
    student_obj.add_school(school_name)
    return True, "选择学校成功！"


def get_course_list_interface(student_name):
    # 获取当前学生对象
    student_obj = models.Student.select(student_name)
    school_name = student_obj.school
    # 判断当前学生是否有学校
    if not school_name:
        return False, "当前学生没有学校，请先联系管理员！"
    # 获取课程列表
    school_obj = models.School.select(school_name)
    # 判断当前学校中是否有课程
    course_list = school_obj.course_list
    if not course_list:
        return False, "当前学生没有课程，请先联系管理员！"
    return True, course_list


def add_course_interface(course_name, student_name):
    # 判断当前学生是否选择课程
    student_obj = models.Student.select(student_name)
    # course_name = student_obj.course_list
    if course_name in student_obj.course_list:
        return False, "该课程已选择，请重新选择!"
    # 调用学生对象中添加课程的方法
    student_obj.add_course(course_name)
    return True, f"{course_name}课程添加成功"


def check_course_interface(student_name):
    student_obj = models.Student.select(student_name)
    if student_obj.score:
        return student_obj.score
