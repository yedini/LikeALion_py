while True:
    num=int(input("구구단 몇단을 계산할까요?\n"))
    if num == 0:
        break
    elif 1<= num <= 9:
        print("구구단 {}단을 계산합니다.".format(num))
        for i in range(1,10):
            print("{}x{}={}".format(num, i, num*i))
    else:
        print('잘못입력했습니다. 1~9 사이 숫자를 입력하세요.')
print('구구단을 종료합니다.')