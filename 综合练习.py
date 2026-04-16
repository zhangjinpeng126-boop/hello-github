"""
    案例:
    开发一个教务管理系统，在该系统中可以维护和管理学员的成绩信息，具体需求如下：
        1. 添加学生信息：根据提示录入学生姓名、语文、数学、英语成绩，录入完成保存到系统中。
        2. 修改学生信息：要求输入要修改的学生姓名，然后再提示输入语文、数学、英语成绩，输入完成后修改学员信息。
        3. 删除学生信息：要求输入要删除的学生姓名，根据姓名删除学生信息。
        4. 查询学生信息：要求输入要查询的学生姓名，根据姓名查询学生信息并输出。
        5. 列出所有学生：遍历所有学生信息并输出。
        6. 统计班级成绩：统计班级语文、数学、英语成绩的最高分、最低分、平均分，以及语文、数学、英语最高分和最低分的学员姓名。
        7. 退出系统。
"""

student_grades = {}
#制作菜单
menu = """
#####################教务管理系统#####################
#                    1.添加学生信息                  #                      
#                    2.修改学生信息                  #
#                    3.删除学生信息                  # 
#                    4.查询学生信息                  #
#                    5.列出所有学生                  #
#                    6.统计班级成绩                  #
#                    7.退出系统                     #
####################################################
"""
print('欢迎使用教务管理系统')

#持续提供系统服务
while True:
    print(menu)

    #具体要执行的操作
    choice=input('请选择具体要执行的操作(1-7):')

    match choice:

        case"1":#添加学生信息
            name=input("请输入要添加的学生姓名:")
            if name in student_grades:
                print('该学生的成绩已添加,请重新选择~')
            else:
                math=float(input("请输入该学生的数学成绩:"))
                chinese=float(input("请输入该学生的语文成绩:"))
                english=float(input("请输入该学生的英语成绩:"))
                student_grades[name]={'Math': math,'Chinese':chinese,'English':english}
                # 字典套字典,外层键是 name，值是另一字典
                print(f"{name}的信息添加成功!")

        case"2":#修改学生信息
            name = input("请输入要修改的学生姓名:")
            if name not in student_grades:
                print('该学生信息不存在,请重新输入!')
                continue
            else:
                chinese = float(input("请输入语文成绩: "))
                math= float(input("请输入数学成绩: "))
                english = float(input("请输入英语成绩: "))
                student_grades[name] = {'Math': math, 'Chinese': chinese, 'English': english}
                print(f"{name}的信息修改成功")

        case "3" :#删除学生信息
            name = input("请输入要删除的学生姓名:")
            if name not in student_grades:
                print('该学生信息不存在,请重新输入!')
            else:
                del student_grades[name]
                print(f"{name}的信息删除成功!")

        case "4" :#查询学生信息
            name = input("请输入要查询的学生姓名:")
            if name not in student_grades:
                print('该学生信息不存在,请重新输入!')
            else:
                grade_info = student_grades[name]
                print(f"学生姓名:{name},数学成绩:{grade_info['Math']},语文成绩:{grade_info['Chinese']},英语成绩:{grade_info['English']}")

        case "5" :#列出所有学生
            for name in student_grades.keys():
                grade_info = student_grades[name]
                print(f"学生姓名:{name},数学成绩:{grade_info['Math']},语文成绩:{grade_info['Chinese']},英语成绩:{grade_info['English']}")

        case "6" :#统计班级成绩:统计班级语文、数学、英语成绩的最高分、最低分、平均分，以及语文、数学、英语最高分和最低分的学员姓名。
            if not student_grades:
                print("系统中暂无学生信息,请先添加学生~")
                continue

            chinese_grade=[]
            math_grade=[]
            english_grade=[]

            for name,grade in student_grades.items():
                chinese_grade.append(grade['Chinese'])
                math_grade.append(grade['Math'])
                english_grade.append(grade['English'])

            chinese_max = max(chinese_grade)
            chinese_min = min(chinese_grade)
            chinese_avg = sum(chinese_grade)/len(chinese_grade)

            math_max = max(math_grade)
            math_min = min(math_grade)
            math_avg = sum(math_grade)/len(math_grade)

            english_max = max(english_grade)
            english_min = min(english_grade)
            english_avg = sum(english_grade)/len(english_grade)

            chinese_max_student = [name for name,grade in student_grades.items() if grade['Chinese'] == chinese_max]
            chinese_min_student = [name for name,grade in student_grades.items() if grade['Chinese'] == chinese_min]
            math_max_student = [name for name,grade in student_grades.items() if grade['Math'] == math_max]
            math_min_student = [name for name,grade in student_grades.items() if grade['Math'] == math_min]
            english_max_student = [name for name,grade in student_grades.items() if grade['English'] == english_max]
            english_min_student = [name for name,grade in student_grades.items() if grade['English'] == english_min]

            print("========班级成绩统计========")

            print(f'语文-最高分:{chinese_max},最低分:{chinese_min},平均分:{chinese_avg:.2f}')
            print(f"最高分的同学:{chinese_max_student},最低分的同学:{chinese_min_student}")

            print(f'数学-最高分:{math_max},最低分:{math_min},平均分:{math_avg:.2f}')
            print(f"最高分的同学:{math_max_student},最低分的同学:{math_min_student}")

            print(f'英语-最高分:{english_max},最低分:{english_min},平均分:{english_avg:.2f}')
            print(f"最高分的同学:{english_max_student},最低分的同学:{english_min_student}")

            print("==========================")
        case "7" :#退出系统
            print('Bye~')
            break

        case _ :
            print('违规操作!请重新输入!')

