def classify(number):
    num=sum(i for i in range(1,number) if number%i==0)
    if number<=0:
        raise ValueError("ValueError")
    elif num==number:
        return "perfect"
    elif num>number:
        return "abundant"
    else:
        return "deficient"


print(classify(1))