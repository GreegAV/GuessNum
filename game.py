print("Игра \"Угадай число!\"")
print("Загадай любое число от 1 до 1000.")
print("Программа будет предлагать варианты, числа.")
print("Если задуманное число больше предложенного, то введи с клавиатуры знак >")
print("Если задуманное число меньше предложенного, то введи с клавиатуры знак <")
print("Если программа угадала - ставь \"!\"")

min = 0
max = 1000
count = 0
while 1 == 1:
    test = (min + max) // 2
    print("Твое число " + str(test) + "? \n")
    sign = input()
    count += 1

    if sign == ">":
        min = test
    if sign == "<":
        max = test
    if sign == "!":
        print("Урааа!!!!!")
        print("Угадано за " + str(count) + " попыток.")
        break
