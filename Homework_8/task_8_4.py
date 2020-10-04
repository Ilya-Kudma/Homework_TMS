mail = "kudma2015@mai.ru"
zen_of_python = """The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!"""

new_string = zen_of_python + "\n" + mail
print(new_string)
# строка для подсчета гласных
newest_string = new_string
string_for_4_task = new_string

# количество всех букв в строке через цикл FOR
letter = 0
for symbol in new_string:
    if symbol.isalpha():
        letter += 1
print(letter)

# количество всех букв в строке через цикл WHILE
bukva = 0
while len(new_string) > 0:
    symbol = new_string[0]
    if "a" <= symbol <= "z" or "A" <= symbol <= "Z":
        bukva += 1
    new_string = new_string[1:]
print(bukva)

# количество гласных в newest_string
newest_string = newest_string.lower()
vowel_letters = "aeyuio"
count = 0
for vowel in newest_string:
    if vowel in vowel_letters:
        count += 1
print(count)

# вывожу каждый 18 символ в зависимости от регистра
every_18th_symbol = string_for_4_task[::18]
for elem in every_18th_symbol:
    if "a" <= elem <= "z":
        print(elem.upper(), ord(elem))
    elif "A" <= elem <= "Z":
        print(elem.lower(), ord(elem))
    else:
        print(elem)
