#Написать программу, которая читая символы из бесконечной последовательности (эмулируется конечным файлом),
#распознает, преобразует и выводит на экран объекты по определенному правилу. 
#Объекты разделены пробелами. Преобразование делать по возможности через словарь.
#Для упрощения под выводом числа прописью подразумевается последовательный вывод всех цифр числа.
#Регулярные выражения использовать нельзя.

#Вариант 13
#Целые числа, содержащие ровно 5 цифр. Вывести количество таких чисел.
#Минимальное число вывести прописью.

digit_map = {
    '-': 'минус', '0': 'ноль', '1': 'один', '2': 'два', '3': 'три', '4': 'четыре',
    '5': 'пять', '6': 'шесть', '7': 'семь', '8': 'восемь', '9': 'девять'
}

count = 0
min_number = float('inf')
current_number = ""
is_negative = False
five_digit_numbers = []

with open('input.txt', 'r') as f:
    while True:
        char = f.read(1)
        if not char:
            break

        if char == '-':
            if not current_number:
                         is_negative = True
            else:
                if current_number and len(current_number) == 5:
                    count += 1
                    number_int = int(current_number)
                    if is_negative:
                        number_int = -number_int
                    min_number = min(min_number, number_int)
                    five_digit_numbers.append(number_int)
                is_negative = False
                current_number = ""

        elif char.isdigit():
            current_number += char
                
        elif current_number:
            if len(current_number) == 5:
                count += 1
                number_int = int(current_number)
                if is_negative:
                    number_int = -number_int
                min_number = min(min_number, number_int)
                five_digit_numbers.append(number_int)
            is_negative = False
            current_number = ""

    if current_number and len(current_number) == 5:
        count += 1
        number_int = int(current_number)
        if is_negative:
            number_int = -number_int
        min_number = min(min_number, number_int)
        five_digit_numbers.append(number_int)
    
if five_digit_numbers:
    print("Найденные 5-значные числа:")
    print(*five_digit_numbers)

print(f"Количество 5-значных чисел: {count}")

if min_number != float('inf'):
    min_number_str = str(min_number)
    print("Минимальное число прописью (цифрами): ", end="")
    for char in min_number_str:
        print(char + ' ' + digit_map[char], end=" ")
else:
    print("Пятизначные числа в файле не найдены.")
