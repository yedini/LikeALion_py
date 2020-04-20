def list_avg(numbers):
    each=numbers.split()
    sum=0
    for n in range(len(each)):
        sum += int(each[n])
    return sum/len(each)

numberlist=input()
print("평균=",list_avg(numberlist))

