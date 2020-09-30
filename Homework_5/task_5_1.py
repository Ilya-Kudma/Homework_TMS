rows = input("Input number: ")
if rows.isdigit():
    rows = int(rows)
    for step in range(rows):
        for star in range(step):
            print("*", end='')
        print("\n")

    for step in range(rows, 0, -1):
        for star in range(step):
            print("*", end='')
        print("\n")
else:
    print("Try again")