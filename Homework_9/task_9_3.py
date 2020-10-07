mail = "kudma2015@mail.ru"
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

# соединенная строка
new_string = lambda x, y: x + '\n' + y
print(new_string(zen_of_python, mail))

# # количество всех букв в строке
string_zen = zen_of_python

import functools

print(functools.reduce(lambda x, y: (x + 1) if y.isalpha() else x, string_zen.lower(), 0))

#  количество гласных в newest_string
print(functools.reduce(lambda x, y: (x + 1) if y in 'aeyiou' else x, string_zen.lower(), 0))

# вывожу каждый 18 символ в зависимости от регистра
every_18th_symbol = lambda x: x[::18].swapcase()
print(every_18th_symbol(string_zen))
