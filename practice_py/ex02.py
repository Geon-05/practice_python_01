def a01(*args) :
    res = 0
    for i in args :
        print("더하는 숫자 :", i)
        res += i
        print("더해진 숫자 :", res)
    print(len(args))
    answer = res/len(args)
    print(answer)
    return answer

def a02(num1) :
    if num1 % 2 == 1 :
        return "홀수입니다."
    else :
        return "짝수입니다."

def a03() :
    pin = input("주민등록번호를 입력하세요").replace("-","")
    
    if len(pin) == 13 and pin[6] in ["1", "2"] :
        yyyymmdd = "19" + pin[:6]
        num = pin[6:]
        print(yyyymmdd)
        print(num)
    elif len(pin) == 13 and pin[6] in ["3", "4"] :
        yyyymmdd = "20" + pin[:6]
        num = pin[6:]
        print(yyyymmdd)
        print(num)
    else :
        print("주민번호를 확인하세요.")

def a04() :
    pin = input("주민등록번호를 입력하세요").replace("-","")
    print(pin[6])

def a05() :
    a = "a:b:c:d"
    b = a.replace(":","#")
    print(b)

def a06() :
    a = [1,3,5,4,2]
    a.sort(reverse=False)
    print(a)
    a.sort(reverse=True)
    print(a)

def a07() :
    a = ['Life', 'is', 'too', 'short']
    result = "".join(a)
    print(result)