list_of_strings = [i for i in input("Input comma separated values: ").split(', ')]
created_list = [f'{element} -  {index}' for (element, index) in enumerate(list_of_strings, 1)]
print(created_list)
