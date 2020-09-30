# Дан словарь: {'test': 'test_value', 'europe': 'eur', 'dollar': 'usd', 'ruble': 'rub'}
# Добавить каждому ключу число равное длине этого ключа (пример {‘key’: ‘value’} ->
# {‘key3’:‘value’}). Чтобы получить список ключей - использовать метод .keys()
my_dictionary = {'test': 'test_value', 'europe': 'eur', 'dollar': 'usd', 'ruble': 'rub'}
print('Initial version: ', my_dictionary)
for key in my_dictionary.keys():
    key1 = key + str(len(key))
    my_dictionary[key1] = my_dictionary.pop(key)
print('Final version: ', my_dictionary)

