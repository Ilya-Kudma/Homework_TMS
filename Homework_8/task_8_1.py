# создаю список из 10 элементов, состоящий из строк
my_list = []
print("Input your list elements: ")
while len(my_list) != 10:
    list_element = input()
    # проверка, может ли быть строка типа int
    if list_element.isdigit():
        list_element = int(list_element)
    my_list.append(list_element)
print(f"My list is {my_list}")


# функция, которая выводит элементы, повторяющиеся только один раз в my_list
def new_list(argument):
    my_new_list = []
    for element in argument:
        if argument.count(element) == 1:
            my_new_list.append(element)
    print(f"My new list -> {my_new_list}")
    return my_new_list


# функция, которая выводит КАЖДЫЙ элемент один раз без повторения
def unique_list(argument):
    new_unique_list = []
    for element in argument:
        if element not in new_unique_list:
            new_unique_list.append(element)
    print(f"My unique list -> {new_unique_list}")
    return new_unique_list


new_list(my_list)
unique_list(my_list)