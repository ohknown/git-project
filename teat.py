def convert_score(grade):
    match grade:
        case 'A+':
            gpa = 4.5
        case 'A':
            gpa = 4.0
        case 'B+':
            gpa = 3.5
        case 'B':
            gpa = 3.0
        case 'C+':
            gpa = 2.5
        case 'C':
            gpa = 2.0
        case 'D+':
            gpa = 1.5
        case 'D':
            gpa = 1.0
        case 'F':
            gpa = 0.0

    return gpa


archive_credit, submit_credit = 0, 0
archive_gpa, submit_gpa = 0.0, 0.0
while True:
    print("작업을 선택하세요.")
    print("1. 입력")
    print("2. 출력")
    
    choice = input()
    value = int(choice)

    match value:
        case 1:
            value = input("학점을 입력하세요: ")
            credit = int(value)
            value = input("평점을 입력하세요: ")
            gpa = convert_score(value)
            print("입력되었습니다.")
            archive_credit += credit
            if gpa > 0:
                submit_gpa += gpa * credit
                submit_credit += credit
                archive_gpa += gpa * credit
                    

        case 2:
            print('제출용: ' + str(submit_credit) + '학점 (GPA: ' + str(submit_gpa / submit_credit) + ')' )
            print('열람용: ' + str(archive_credit) + '학점 (GPA: ' + str(archive_gpa / archive_credit) + ')')
            print("프로그램을 종료합니다.")
            break
