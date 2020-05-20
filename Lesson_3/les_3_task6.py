# 6. Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же,
# но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.
# Продолжить работу над заданием. В программу должна попадать строка из слов,
# разделенных пробелом. Каждое слово состоит из латинских букв в нижнем регистре.
# Сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы.
# Необходимо использовать написанную ранее функцию int_func().


def int_func(word):
    new_word_total = ""
    word_list = word.split()
    for word_ in word_list:
        new_word = ""
        for x in word_:
            if 97 <= ord(x) <= 122:
                new_word = new_word + x
            else:
                print(f"Пропущена другая буква! - {x}")
        new_word_total = new_word_total + new_word.title() + " "
    return new_word_total


print(int_func("text"))
