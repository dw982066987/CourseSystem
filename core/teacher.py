"""老师视图"""
from core import src
from lib import common
from interface import common_interface
from interface import teacher_interface

teacher_info = {
    "user": None
}


def logout():
    print("谢谢使用".center(50, "="))
    exit()


def back_index():
    src.run()


def login():
    while True:
        username = input("请输入用户名:").strip()
        password = input("请输入密码:").strip()
        flag, msg = common_interface.login_interface(username, password, user_type="teacher")
        if flag:
            teacher_info["user"] = username
            print(msg)
            break
        else:
            print(msg)
            break


@common.auth("teacher")
def check_course():
    while True:
        flag, msg = teacher_interface.check_course_list_interface(teacher_info.get("user"))
        if flag:
            print(msg)
            break
        else:
            print(msg)
            break


@common.auth("teacher")
def choose_course():
    while True:
        # 选择学校
        flag, school_list = common_interface.get_all_school_interface()
        if not flag:
            print(school_list)
            break
        for index, school_name in enumerate(school_list):
            print(f"编号{index}，学校名{school_name}")
        choice = input("请输入学校编号：").strip()
        if not choice.isdigit():
            print("请输入正确编号！")
            continue
        choice = int(choice)
        if choice not in range(len(school_list)):
            print("输入的编号有误！")
            continue
        school_name = school_list[choice]
        # 从学校获取课程
        flag2, course_list = common_interface.get_course_in_school_interface(school_name)
        if not flag2:
            print(course_list)
            break

        for index2, course_name in enumerate(course_list):
            print(f"编号{index2}，学校名{course_name}")
        choice2 = input("请输入课程编号：").strip()
        if not choice2.isdigit():
            print("请输入正确编号！")
            continue
        choice2 = int(choice)
        if choice2 not in range(len(course_list)):
            print("输入的编号有误！")
            continue
        course_name = course_list[choice2]
        # 调用选择教授课程接口，将课程添加老师课程列表
        flag3, msg = teacher_interface.add_course_interface(course_name, teacher_info.get("user"))
        if flag3:
            print(msg)
            break
        else:
            print(msg)
            break


@common.auth("teacher")
def check_stu_from_course():
    pass


@common.auth("teacher")
def change_score_from_student():
    pass


func_dict = {
    "0": logout,
    "1": login,
    "2": check_course,
    "3": choose_course,
    "4": check_course,
    "5": change_score_from_student,
    "6": back_index
}


def teacher_view():
    # 管理主界面
    while True:
        print("欢迎来到教师界面".center(47, "="))
        print("""
                     0、退出
                     1、登录
                     2、查看教授课程
                     3、选择教授课程
                     4、查看课程下学生
                     5、修改学生成绩 
                     6、返回主页                         
         """)
        print("=" * 53)

        choice = input("请输入功能编号：").strip()

        if choice not in func_dict:
            print("请输入正确编号！")
            continue
        func_dict.get(choice)()
