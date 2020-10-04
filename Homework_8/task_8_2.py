def letters(new_string):
    lower_case = 0
    upper_case = 0
    new_dictionary = {}
    while len(new_string) > 0:
        symbol = new_string[0]
        if "a" <= symbol <= "z":
            lower_case += 1
        elif "A" <= symbol <= "Z":
            upper_case += 1
        new_string = new_string[1:]
    new_dictionary["Uppercase letters"] = upper_case
    new_dictionary["Lowercase letters"] = lower_case
    print(new_dictionary)
    return new_dictionary


my_string = input('Please, input a string: ')
letters(my_string)
