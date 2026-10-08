year = int(input("Enter a year: "))
for year in range (0, 2026, 4):
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        print(year)