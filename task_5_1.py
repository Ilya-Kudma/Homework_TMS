rows = input("Input number: ")
if rows.isdigit():
    for step in range(int(rows)):
        for star in range(step):
            print("*", end='')
        print("\n")

    for step in range(int(rows), 0, -1):
        for star in range(step):
            print("*", end='')
        print("\n")
else:
    print("Try again")