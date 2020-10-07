# Создать lambda функцию, которая принимает на вход неопределенное
# количество именных аргументов и выводит словарь с ключами удвоенной
# длины. {‘abc’: 5} -> {‘abcabc’: 5
my_dictionary = {'one': '1', 'two': '2', 'three': '3'}
print(dict(map(lambda x, y: (x*2, y), my_dictionary.keys(), my_dictionary.values())))


def print_values(**kwargs):
    for key, value in kwargs.items():
        dict_ = {key * 2: value}
        print(dict_)


print_values(string="one", integer=1, float=2.0)