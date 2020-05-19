"""学员视图"""
from core import src


def logout():
    print("谢谢使用".center(50, "="))
    exit()


def back_index():
    src.run()


def register():
    pass


def login():
    pass


def choice_school():
    pass


def choice_course():
    pass


def check_score():
    pass


func_dict = {
    "0": logout,
    "1": register,
    "2": login,
    "3": choice_school,
    "4": choice_course,
    "5": check_score,
    "6": back_index
}


def student_view():
    # 管理主界面
    while True:
        print("欢迎来到学员界面".center(47, "="))
        print("""
                     0、退出
                     1、注册
                     2、登录
                     3、选择校区
                     4、选择课程
                     5、查看成绩    
                     6、返回主页          
         """)
        print("=" * 53)

        choice = input("请输入功能编号：").strip()

        if choice not in func_dict:
            print("请输入正确编号！")
            continue
        func_dict.get(choice)()