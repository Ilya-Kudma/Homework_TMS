# Составить список чисел Фибоначчи содержащий 15 элементов.
# With "while"
f1 = int(input('Input value: '))
f2 = f1
i = 0
fibonacci = [f1, f2]
while i < 13:
    f_sum = f1 + f2
    fibonacci.append(f_sum)
    f1 = f2
    f2 = f_sum
    i += 1
print(fibonacci, "\n\n")

# With "for"
f2 = f1 = 1
sum_ = f1+f2
fibonacci = [f1, f2]
for i in range(sum_, 15, 1):
    fibonacci.append(fibonacci[i-1]+fibonacci[i-2])
print(fibonacci)
