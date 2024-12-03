# Question 5
# Create a Command-Line Interface (CLI) project in Python that mimics Safaricom's SIM Toolkit. When you run the program, it should display menus dynamically based on user input. The program should handle user choices and navigate through different options just like the Safaricom SIM Toolkit.

# Requirements:
# Main Menu: When the program starts, display the following options:
# SIM 1
# 1. Safaricom
# 2. M-PESA
# Enter your choice: ________

# Submenu for M-PESA: If the user selects option 1 (M-PESA), show the following menu:
# SIM 1
# 1. Send Money
# 2. Withdraw Cash
# 3. Buy Airtime
# 4. Loans and Savings
# 5. Lipa na M-PESA
# 6. My Account
# Enter your choice: ________

# Submenu for "Send Money": If the user selects option 1 (Send Money), display:
# Enter Phone Number: 
# (Digits 0-9, *, #, +) 
# 10-13 characters: 
# ________________
# After each action, the program should handle input validation and navigate back to the appropriate menu or exit the program if the user wishes.
# Example Interaction:
# - User runs the program this displays in the terminal :
# SIM 1
# 1. Safaricom
# 2. M-PESA
# Enter your choice: 2

# - Next screen appears:
# SIM 1
# 1. Send Money
# 2. Withdraw Cash
# 3. Buy Airtime
# 4. Loans and Savings
# 5. Lipa na M-PESA
# 6. My Account
# Enter your choice: 1

# - Next screen appears:
# Enter Phone Number:
# (Digits 0-9, *, #, +)
# 10-13 characters: ________

# Validate inputs where necessary (e.g., valid phone numbers, numeric entries for options).
# Allow users to navigate back to previous menus or exit the program.
# HINT
# You use several functions, if else statements etc
# Getting user inputs in terminal i.e using  input("Enter your calculation: ")
