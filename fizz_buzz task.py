# 1 - 100
# 3 - Fizz
# 5 - Buzz
# 3 & 5 - FizzBuzz
# 1


def fizz_buzz(i):
    if not (i % 3) and not (i % 5):  # означает что если i кратное 3-м и  означает что если i кратное 5-ти
        print('FizzBuzz')
    elif i % 3 == 0:  # означает что если i кратное 3-м
        print('Fizz')
    elif i % 5 == 0:  # означает что если i кратное 5-ти
        print('Buzz')
    else:
        print(i)

i = range(0, 101)
fizz_buzz(i)