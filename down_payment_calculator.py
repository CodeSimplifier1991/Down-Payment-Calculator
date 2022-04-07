# Get the client name from the console
get_theClientName = input("What is your name? ")

# Gree the client after getting their name
print(f'Hi, {get_theClientName}')

# Get the car price from the console and convert it to float
get_carPrice = float(input("What is the cost of the car? "))

# Check if there is an outstanding balance then convert the response to lower case
is_thereOutstandingBalance = input("Do you have any outstanding balance with us? (Yes/No) ").lower()

# Initialize the down payment and default message
downPayment = 0
message = ""

# If there is an outstanding balance
if is_thereOutstandingBalance == 'yes':

    # Down payment would be 20% of the car price
    downPayment = get_carPrice * 0.2

    # The message with the down payment amount will be shown as a message
    message = f"{get_theClientName}, you need ${downPayment} as down payment."

# There is no outstanding balance
else:

    # Down payment would be 10% of the car price
    downPayment = get_carPrice * 0.1

    # The message with the down payment amount will be shown as a message
    message = f"{get_theClientName}, you need ${downPayment} as down payment."

# The message with the down payment will be shown to client
print(message)

