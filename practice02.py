def convert_score(grade):
    match grade:
        case 'A+':
            return 4.5
        case 'A':
            return 4.0
        case 'B+':
            return 3.5
        case 'B':
            return 3.0
        case 'C+':
            return 2.5
        case 'C':
            return 2.0
        case 'D+':
            return  1.5
        case 'D':
            return 1.0
        case 'F':
            return 0.0


archive_credit, submit_credit = 0, 0
archive_gpa, submit_gpa = 0.0, 0.0
dict_subject = {'오픈소스SW와 파이썬 프로그래밍' : '1', 'CAU세미나' : '2', '글쓰기' : '3', 'COMMUNICATION IN ENGLISH' : '4',
                '기초컴퓨터프로그래밍' : '5', '미적분학' : '6', '일반물리(1)' : '7', '일반물리실험(1)' : '8', '창의적설계' : '9'}
sw = {value:key for key, value in dict_subject.items()}
course = []
i = 1
    
while True:
    print("작업을 선택하세요.")
    print("1. 입력")
    print("2. 출력")
    print("3. 계산")
    
    choice = int(input())

    match choice:
        case 1:
            print('과목명을 입력하세요: ')
            subject = input()
            value = input("학점을 입력하세요: ")
            credit = int(value)
            value = input("평점을 입력하세요: ")
            gpa = convert_score(value)
            print("입력되었습니다.")
            
            if i > 1:
                for repeat in range(i-1):
                    if int(course[repeat][0]) == int(dict_subject[subject]):
                        if convert_score(course[repeat][2]) < gpa:
                            print(course[repeat][2])
                    else:
                        info = (dict_subject[subject], credit, value)
                        course.append(info)
                        i += 1
                        archive_credit += credit
                        archive_gpa += gpa * credit
                        if gpa > 0:
                            submit_gpa += gpa * credit
                            submit_credit += credit
            elif i == 1:
                info = (dict_subject[subject], credit, value)
                course.append(info)
                i += 1
                archive_credit += credit
                archive_gpa += gpa * credit
                if gpa > 0:
                    submit_gpa += gpa * credit
                    submit_credit += credit   

        case 2:
            for repeat in range(i-1):
                print('[' + sw[course[repeat][0]] + ']', '{0}학점: {1}'.format(course[repeat][1], course[repeat][2]))

        case 3:
            print('제출용: ' + str(submit_credit) + '학점 (GPA: ' + str(submit_gpa / submit_credit) + ')' )
            print('열람용: ' + str(archive_credit) + '학점 (GPA: ' + str(archive_gpa / archive_credit) + ')')
            break

print("프로그램을 종료합니다.")