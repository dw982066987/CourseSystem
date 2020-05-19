"""用户视图层"""
from core import admin
from core import student
from core import teacher


def logout():
    print("谢谢使用".center(50, "="))
    exit()


# 创建功能字典
func_dict = {
    "0": logout,
    "1": admin.admin_view,
    "2": student.student_view,
    "3": teacher.teacher_view,
}


def run():
    # 用户主界面
    while True:
        print("欢迎来到选课系统".center(47, "="))
        print("""
                     0、退出
                     1、管理员功能
                     2、学生功能
                     3、老师功能 
        """)
        print("=" * 53)
        # 用户选择功能
        choice = input("请输入功能编号：").strip()

        if choice not in func_dict:
            print("请输入正确编号！")
            continue
        func_dict.get(choice)()
