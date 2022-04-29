# Created by: Ferdous Sediqi
# Created on: April. 27 2022
# created by: Ferdous Sediqi
# This program asks the user to enter a positive number
# and then uses a loop to calculate and display the sum
# of all numbers from 0 until that number also display invalid input

def main():
    while True:
        # Declaring variables
        counter = 0
        total_sum = 0

        # Ask user how many numbers they want to add up
        user_input = input("How many numbers would you like to enter?: ")

        try:
            # Casting to int
            user_input_as_int = int(user_input)
            # Check if the input is a positive number
            if user_input_as_int <= 0:
                print(
                    "Invalid number. Input cannot be 0 or less."
                )
                break

        except Exception:
            # If the user enters a invalid input
            print("Invalid number. Please input a positive number.")
            break

        while counter < user_input_as_int:

            # Ask user to input their number
            user_num = input("Enter a number: ")

            try:
                # Casting to int
                user_num_as_int = int(user_num)

                # Check if the input is a positive number
                if user_num_as_int <= 0:
                    print(
                        "Invalid number. Input cannot be 0 or less."
                    )
                    continue

                # Add user numbers
                total_sum = total_sum + user_num_as_int
                # counter+1
                counter += 1

            except Exception:
                # If the user enters a invalid input
                print("Invalid number. Enter a number.")

        # Display total sum
        print("The total sum of the numbers is {}.".format(total_sum))
        break


if __name__ == "__main__":
    main()
