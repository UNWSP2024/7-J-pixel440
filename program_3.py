# Program #3: US_Population
def main():
    # Have the user input (using a loop) various information that contains three pieces of data:
    # year, name of state, and population.
    # Store all of this information in a list of lists.  For example it might be stored like this:

    all_entered_values = []
    while True:
    # Now have the user enter a year.
        year = input("Enter the year (or 'no' to end): ")
        if year.lower() == 'no':
            break
        state = input("Enter state: ")
        population = int(input("Enter population: "))

    all_entered_values.append([int(year), state, population])


    year = int(input("Enter the year to calculate total population: "))

    total_population = sum(item[2] for item in all_entered_values if item[0] == year)

    print(f"Total population in {year}: {total_population}.")
# The program will add the populations from all states in the list of list for that year only.
# Pass the list and year to the sum_population_for_year

# Loop through and sum the populations for the appropriate year.
# e.g. for the list on line 7 the total would be 8,860,637 if the user enterd 2010 for the year to sum,
# or 3,421,988 if they enterd 2011 for the year to sum.

# print the totalled population


# Call the main function.
if __name__ == '__main__':
    main()
