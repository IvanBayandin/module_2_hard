def password(number):
    pass_ = ' '
    for i in range(1, number):
        for j in range(i + 1, number):
            if number % (i + j) == 0:
                pass_ += str(i) + str(j)
    return pass_
import random

num = random.randint(3, 20)
print('Число из первой вставки: ', num)
result = password(num)
if result:
    for pass_ in result:
        print(pass_, end = '')

