# This program demonstrates how to center-align strings.
name1 = 'Gordon'
name2 = 'Smith'
name3 = 'Washington'
name4 = 'Alvarado'
name5 = 'Livingston'
name6 = 'Jones'

# Display the names.
print(f'***{name1:^20}***')
print(f'***{name2:^20}***')
print(f'***{name3:^20}***')
print(f'***{name4:^20}***')
print(f'***{name5:^20}***')
print(f'***{name6:^20}***')

# This program displays the following numbers
# in two columns.
num1 = 127.899
num2 = 3465.148
num3 = 3.776
num4 = 264.821
num5 = 88.081
num6 = 799.999

# Each number is displayed in a field of 10 spaces
# and rounded to 2 decimal places.
print(f'{num1:10.2f}{num2:10.2f}')
print(f'{num3:10.2f}{num4:10.2f}')
print(f'{num5:10.2f}{num6:10.2f}')

# This program displays a person's
# name and address.
print('Kate Austen')
print('123 Full Circle Drive')
print('Asheville, NC 28899')

# This program demonstrates string concatenation.
first_name = input('Enter your first name: ')
last_name = input('Enter your last name: ')

# Combine the names with a space between them.
full_name = first_name + ' ' + last_name

# Display the user's full name.
print('Your full name is ' + full_name)

print('Your assignment is to read "Hamlet" by tomorrow.')

# This program demonstrates how a floating-point
# number can be displayed as currency.
monthly_pay = 5000.0
annual_pay = monthly_pay * 12
print(f'Your annual pay is ${annual_pay:,.2f}')

# This program demonstrates how a floating-point
# number is displayed with no formatting.
amount_due = 5000.0
monthly_payment = amount_due / 12.0
print(f'The monthly payment is {monthly_payment}.')
# This program demonstrates how a floating-point
# number can be formatted.
amount_due = 5000.0
monthly_payment = amount_due / 12
print('The monthly payment is', \
      format(monthly_payment, '.2f'))
