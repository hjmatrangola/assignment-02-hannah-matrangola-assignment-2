# Programmer: Hannah Matrangola
# Course: CS151, Prof. Mehri
# Date: 10/6/21
# Programming Assignment: 2
# Program Inputs: Month and Year
# Program Outputs: The number of days in that month.


month_number = int(input("Enter Month number: "))
year = int(input("Enter the year: "))

if month_number <=0 or month_number > 12:
    print("Error")

else:
    if month_number == 1 or month_number == 3 or month_number == 5 or month_number == 7 or month_number == 8 or month_number == 10 or month_number == 12:
        print("Number of days: 31")

    else:
        if month_number == 4 or month_number == 6 or month_number == 9 or month_number == 11:
            print("Number of days: 30")

    if month_number <= 0 or month_number > 12:
        print("Error")

    else:
        if month_number == 2:
            if (year % 4) == 0:
                if (year % 100) == 0:
                    if (year % 400) == 0:
                        print("Number of days: 29")
                    else:
                        print("Number of days: 28")
                else:
                    print("Number of days: 29")

            else:
                print("Number of days: 28")
