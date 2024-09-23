import ex01
import ex02

while True :
    answer = input("실행 할 함수 그룹번호를 입력하세요.")
    
    if answer == "01" :
        ex01.print_hello()
        ex01.hypotenuse(550, 600)
        ex01.fileSize(800, 110)
        ex01.test01()
        ex01.write_data()
        ex01.read_data()
        ex01.add_data()
        ex01.autoClose_data()
    elif answer == "02" :
        ex02.a01(80,75,55)
        print(ex02.a02(80))
    else :
        print("아직 함수를 만들고있어요!")
        exit()