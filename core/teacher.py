"""老师视图"""
from core import src


def logout():
    print("谢谢使用".center(50, "="))
    exit()


def back_index():
    src.run()


def login():
    pass


def check_course():
    pass


def choose_course():
    pass


def check_stu_from_course():
    pass


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