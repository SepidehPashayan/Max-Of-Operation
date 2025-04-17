def get_numbers():
    numbers=[]
    while True:
        number=input()
        num=number.split("?")
        if len(num)!=3:
            print("the number of character is not correct")
            continue
        try:
            numbers=list(map(int,num))
            return numbers
        except ValueError:
            print("please just enter numbers")

def maxi(numbers):
    maximum=numbers[0]*numbers[1]*numbers[2]
    temp=numbers[0]*numbers[1]+numbers[2]
    if temp>maximum:
        maximum=temp
    temp=numbers[0]+numbers[1]*numbers[2]
    if temp>maximum:
        maximum=temp
    temp=numbers[0]*(numbers[1]+numbers[2])
    if temp>maximum:
        maximum=temp
    temp=(numbers[0]+numbers[1])*numbers[2]
    if temp>maximum:
        maximum=temp
    temp=numbers[0]+numbers[1]+numbers[2]
    if temp>maximum:
        maximum=temp
    return maximum

final=get_numbers()
print(maxi(final))