# Дан список. Создать новый список, сдвинутый на 1 элемент влево
# Пример: 1 2 3 4 5 -> 2 3 4 5 1
# With "while"
my_list = list(range(1, 6, 1))
print(my_list)
new_list = []
i = 1
while i < len(my_list):
    new_list.append(my_list[i])
    i += 1
new_list.append(my_list[0])
print(new_list, "\n\n")

# With "for"
my_list = list(range(1, 6, 1))
print(my_list)
new_list = []
for i in my_list:
    new_list.append(i)
new_list.append(new_list[0])
new_list.pop(0)
print(new_list)

