# Program #1: Rainfall
# Design a program that lets the user enter the total rainfall for each of 12 months into a list.
# The program should calculate and display the total rainfall for the year, 
# the average monthly rainfall, # and the months with the highest and lowest amounts.
def main():
    rain = []
    print("Enter total rainfall for each month this year.")
    for month in range(1,13):
        while True:
            try:
                user_input = float(input(f"Rain for month {month}:"))
                if user_input < 0:
                    print("The number must be greater than zero, please try again")
                    continue


                rain.append(user_input)
                break

            except ValueError:
                print("Please enter a positive number")

    total_rainfall=sum(rain)
    avg_rainfall=total_rainfall/12
    most=max(rain)
    least=min(rain)
    highest_month=rain.index(most)+1
    lowest_month=rain.index(least)+1

    print(f"The total rain fall this year was {total_rainfall} inches")
    print(f"the average rain fall this year was {avg_rainfall} inches")
    print(f"the month with the most rain was month {highest_month}")
    print(f"the month with the least rain was month {lowest_month}")

if __name__=="__main__":
    main()
