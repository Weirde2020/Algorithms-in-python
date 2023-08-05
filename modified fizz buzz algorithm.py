# Creating a fizz buzz algorithm modified
# Write a function that loops through the user's input
def fizz_buzz(start_range, end_range):
    for i in range(start_range, end_range):
        if i % 3 == 0 and i % 5 == 0:
            print("Fizzbuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

if __name__ == "__main__":
    # Ask user for the first number
    start_range = int(input("Enter the first number: "))
    # Ask user for the last number 
    end_range = int(input("Enter the last number: "))
# Show your output 
    fizz_buzz(start_range, end_range)
