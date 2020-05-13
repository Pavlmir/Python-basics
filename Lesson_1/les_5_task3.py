# 3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
# Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.
# 3 + 33 + 333 = 3*1+0 + 3*10+3 + 3*100+33
num = int(input("Введите число:"))
sum_num = 0
numbers = []
str_num = ""
while len(numbers) != num:
    str_num = str_num + str(num)
    sum_num += int(str_num)
    numbers.append(str_num)

print(f"Считаем: {' + '.join(numbers)} = {sum_num:,}".replace(',', ' '))
