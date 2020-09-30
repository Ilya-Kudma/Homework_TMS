# Конвертирую значение, вводиммые с клавиатуры.
# Далее с 1 по 121 строки кода операции аналогичные.
def inches_to_centimeters():
    # Проверяю, что вводится корректное значение.
    try:
        inches = float(input("Input inches: "))
        centimeters = inches * 2.54
        print(f"{inches} inches is {centimeters} centimeters")
        return centimeters
    except ValueError:
        print("You must input only digits")


def centimeters_to_inches():
    try:
        centimeters = float(input("Input centimeters: "))
        inches = centimeters / 2.54
        print(f"{centimeters} centimeters is {inches} inches")
        return inches
    except ValueError:
        print("You must input only digits")


def miles_to_kilometers():
    try:
        miles = float(input("Input miles: "))
        kilometers = miles * 1.609
        print(f"{miles} miles is {kilometers} kilometers")
        return kilometers
    except ValueError:
        print("You must input only digits")


def kilometers_to_miles():
    try:
        kilometers = float(input("Input kilometers: "))
        miles = kilometers / 1.609
        print(f"{kilometers} kilometers is {miles} miles")
        return miles
    except ValueError:
        print("You must input only digits")


def pounds_to_kilograms():
    try:
        pounds = float(input("Input pounds: "))
        kilograms = pounds / 2.205
        print(f"{pounds} pounds is {kilograms} kilograms")
        return kilograms
    except ValueError:
        print("You must input only digits")


def kilograms_to_pounds():
    try:
        kilograms = float(input("Input kilograms: "))
        pounds = kilograms * 2.205
        print(f"{kilograms} kilograms is {pounds} pounds")
        return pounds
    except ValueError:
        print("You must input only digits")


def ounces_to_grams():
    try:
        ounces = float(input("Input ounces: "))
        grams = ounces * 28.35
        print(f"{ounces} ounces is {grams} grams")
        return grams
    except ValueError:
        print("You must input only digits")


def grams_to_ounces():
    try:
        grams = float(input("Input grams: "))
        ounces = grams / 28.35
        print(f"{grams} grams is {ounces} ounces")
        return ounces
    except ValueError:
        print("You must input only digits")


def gallon_to_liter():
    try:
        gallon = float(input("Input gallon: "))
        liter = gallon * 3.785
        print(f"{gallon} gallon is {liter} liter")
        return liter
    except ValueError:
        print("You must input only digits")


def liter_to_gallon():
    try:
        liter = float(input("Input liter: "))
        gallon = liter / 3.785
        print(f"{liter} liter is {gallon} gallon")
        return gallon
    except ValueError:
        print("You must input only digits")


def pint_to_liter():
    try:
        pint = float(input("Input pint: "))
        liter = pint / 1.76
        print(f"{pint} pint is {liter} liter")
        return liter
    except ValueError:
        print("You must input only digits")


def liter_to_pint():
    try:
        liter = float(input("Input liter: "))
        pint = liter * 1.76
        print(f"{liter} liter is {pint} pint")
        return pint
    except ValueError:
        print("You must input only digits")


print("1. inches to centimeters",
      "2. centimeters to inches",
      "3. miles to kilometers",
      "4. kilometers to miles",
      "5. pounds to kilograms",
      "6. kilograms to pounds",
      "7. ounces to grams",
      "8. grams to ounces",
      "9. gallons to liters",
      "10. liters to gallons",
      "11. pints to liters",
      "12. liters to pints",
      sep="\n")


# Создаю фунцию для последующих вариантов конвертации значений.
def repeat_input():
    try:
        value_number = int(input("Input your number from 1 to 12: "))
        return value_number
    except ValueError:
        print("Please, input only integer value!")


your_number = repeat_input()

while your_number != 0:
    if your_number == 1:
        inches_to_centimeters()
        your_number = repeat_input()
    elif your_number == 2:
        centimeters_to_inches()
        your_number = repeat_input()
    elif your_number == 3:
        miles_to_kilometers()
        your_number = repeat_input()
    elif your_number == 4:
        kilometers_to_miles()
        your_number = repeat_input()
    elif your_number == 5:
        pounds_to_kilograms()
        your_number = repeat_input()
    elif your_number == 6:
        kilograms_to_pounds()
        your_number = repeat_input()
    elif your_number == 7:
        ounces_to_grams()
        your_number = repeat_input()
    elif your_number == 8:
        grams_to_ounces()
        your_number = repeat_input()
    elif your_number == 9:
        gallon_to_liter()
        your_number = repeat_input()
    elif your_number == 10:
        liter_to_gallon()
        your_number = repeat_input()
    elif your_number == 11:
        pint_to_liter()
        your_number = repeat_input()
    elif your_number == 12:
        liter_to_pint()
        your_number = repeat_input()
    else:
        your_number = repeat_input()

print("You're out of the program")
