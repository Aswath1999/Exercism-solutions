def is_armstrong_number(number):
    arms=0
    for i in str(number):
        arms+=int(i)**(len(str(number)))
    return arms==number


number=154
print(is_armstrong_number(number))