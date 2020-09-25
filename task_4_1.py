# Дан список целых чисел.
# Создать новый список, каждый элемент которого равен исходному элементу
# умноженному на -2
# With "for"
my_list = list(range(41, 4, -2))
print(my_list)
my_new_list = []
for i in my_list:
    i *= -2
    my_new_list.append(i)
print(my_new_list, "\n\n")


# WIth "while"
my_list = list(range(41, 4, -2))
print(my_list)
my_new_list = []
index_ = 0
while index_ < len(my_list):
    my_list[index_] *= -2
    my_new_list.append(my_list[index_])
    index_ += 1
print(my_new_list)