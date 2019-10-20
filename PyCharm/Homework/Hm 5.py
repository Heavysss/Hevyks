# Программа для выявления палиндром в веденном тексте
# Программа не готова так как она не умеет убирать знаки пунктуации и пробелы
# V2 Программа работает как должна

def reverse(text):      # Функция для переворота строки
    return text[::-1]

def is_palindrome(text):    # Функция для сравнения
    return text == reverse(text)
something = input('Введите текст: ')    # Ввод палиндром

def clear(something):       # Функция для очистки лишнего
    someth1 = something.replace(" ","")     # Удаление пробелов
    someth1 = someth1.lower()       # Опускает все заглавные буквы
    someth1 = someth1.replace(",","")   # Убирает запятые
    return someth1

if (is_palindrome(clear(something))):  # Условие для вывода
    print('Да, это палиндроме')
else:
    print('Нет, это не палиндроме')

