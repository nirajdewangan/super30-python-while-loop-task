# while Loop Mastery
# Super30 Python Task


# ==================================================
# Question 1
# Print numbers from 1 to 100 using while
# Initialization: number = 1
# Condition: number <= 100
# Update: number += 1
# ==================================================

print("\n--- Question 1: Numbers from 1 to 100 ---")

number = 1

while number <= 100:
    print(number, end=" ")
    number += 1

print()


# ==================================================
# Question 2
# Print numbers from 100 to 1
# Initialization: number = 100
# Condition: number >= 1
# Update: number -= 1
# ==================================================

print("\n--- Question 2: Numbers from 100 to 1 ---")

number = 100

while number >= 1:
    print(number, end=" ")
    number -= 1

print()


# ==================================================
# Question 3
# Print even numbers from 1 to 100
# Initialization: number = 2
# Condition: number <= 100
# Update: number += 2
# ==================================================

print("\n--- Question 3: Even Numbers ---")

number = 2

while number <= 100:
    print(number, end=" ")
    number += 2

print()


# ==================================================
# Question 4
# Calculate sum of digits
# Example: 5832 -> 18
# ==================================================

print("\n--- Question 4: Sum of Digits ---")

number = int(input("Enter a number: "))

temp = abs(number)
digit_sum = 0

# Condition: continue while digits remain
while temp > 0:
    digit = temp % 10
    digit_sum += digit
    temp //= 10

print("Sum of Digits:", digit_sum)


# ==================================================
# Question 5
# Reverse an integer using while
# Example: 12345 -> 54321
# ==================================================

print("\n--- Question 5: Reverse an Integer ---")

number = int(input("Enter an integer to reverse: "))

temp = abs(number)
reversed_number = 0

while temp > 0:
    digit = temp % 10
    reversed_number = reversed_number * 10 + digit
    temp //= 10

if number < 0:
    reversed_number = -reversed_number

print("Reversed Integer:", reversed_number)


# ==================================================
# Question 6
# Count digits in an integer
# ==================================================

print("\n--- Question 6: Count Digits ---")

number = int(input("Enter an integer to count digits: "))

temp = abs(number)
digit_count = 0

if temp == 0:
    digit_count = 1
else:
    while temp > 0:
        digit_count += 1
        temp //= 10

print("Number of Digits:", digit_count)


# ==================================================
# Question 7
# Calculate factorial using while
# ==================================================

print("\n--- Question 7: Factorial ---")

number = int(input("Enter a number for factorial: "))

if number < 0:
    print("Factorial is not defined for negative numbers.")

else:
    factorial = 1
    i = 1

    # Initialization: i = 1
    # Condition: i <= number
    # Update: i += 1
    while i <= number:
        factorial *= i
        i += 1

    print("Factorial of", number, "is:", factorial)


# ==================================================
# Question 8
# Keep asking for numbers until user enters 0
# Display sum of previous numbers
# ==================================================

print("\n--- Question 8: Sum Until Zero ---")

total = 0

number = int(input("Enter a number (0 to stop): "))

# Termination happens when user enters 0
while number != 0:
    total += number

    number = int(input("Enter another number (0 to stop): "))

print("Total Sum:", total)


# ==================================================
# Question 9
# Password checker
# Keep asking until password is correct
# ==================================================

print("\n--- Question 9: Password Checker ---")

correct_password = "python123"

password = input("Enter password: ")

# Loop continues while password is incorrect
while password != correct_password:
    print("Incorrect password. Try again.")

    password = input("Enter password: ")

print("Password correct. Access granted!")


# ==================================================
# Question 10
# Guessing Game
# ==================================================

print("\n--- Question 10: Number Guessing Game ---")

secret_number = 27

guess = int(input("Guess the secret number: "))

# Loop continues until correct guess
while guess != secret_number:

    if guess < secret_number:
        print("Too low!")

    else:
        print("Too high!")

    guess = int(input("Try again: "))

print("Correct! You guessed the secret number.")


# ==================================================
# Question 11
# Menu-driven Calculator
# Menu continues until Exit
# ==================================================

print("\n--- Question 11: Menu-Driven Calculator ---")

choice = ""

while choice != "5":

    print("\n--- CALCULATOR MENU ---")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "5":
        print("Exiting Calculator.")
        break

    if choice in ["1", "2", "3", "4"]:

        first_number = float(input("Enter first number: "))
        second_number = float(input("Enter second number: "))

        if choice == "1":
            print("Result:", first_number + second_number)

        elif choice == "2":
            print("Result:", first_number - second_number)

        elif choice == "3":
            print("Result:", first_number * second_number)

        elif choice == "4":

            if second_number == 0:
                print("Cannot divide by zero.")

            else:
                print("Result:", first_number / second_number)

    else:
        print("Invalid choice. Please select 1 to 5.")


# ==================================================
# Question 12
# ATM Menu using while
# Continues until user chooses Exit
# ==================================================

print("\n--- Question 12: ATM Simulation ---")

balance = 10000

choice = ""

while choice != "4":

    print("\n--- ATM MENU ---")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        print("Current Balance: ₹", balance)

    elif choice == "2":

        amount = float(input("Enter deposit amount: ₹"))

        if amount > 0:
            balance += amount
            print("Deposit successful.")
            print("Updated Balance: ₹", balance)

        else:
            print("Invalid deposit amount.")

    elif choice == "3":

        amount = float(input("Enter withdrawal amount: ₹"))

        if amount <= 0:
            print("Invalid withdrawal amount.")

        elif amount > balance:
            print("Insufficient balance.")

        else:
            balance -= amount
            print("Withdrawal successful.")
            print("Remaining Balance: ₹", balance)

    elif choice == "4":
        print("Thank you for using the ATM.")

    else:
        print("Invalid choice. Please select 1 to 4.")


print("\nAll While Loop Mastery Programs Completed!")