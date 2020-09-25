# Дан список целых чисел. Подсчитать сколько четных чисел в списке
# With "for"
my_list = list(range(1, 35, 3))
print(my_list)
quantity = 0
for i in my_list:
    if i % 2 == 0:
        quantity += 1
print(f'Even numbers quantity = {quantity}\n\n')

# With  "while"
my_list = list(range(1, 35, 3))
print(my_list)
quantity = 0
i = 0
while i < len(my_list):
    if i % 2 == 0:
        quantity += 1
    i += 1
print(f"Even numbers quantity = {quantity}")
