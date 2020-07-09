# mortgage.py
#
# Exercise 1.7

"""
- Part 1
Dave has decided to take out a 30-year fixed rate mortgage of $500,000 with Guido’s Mortgage, 
Stock Investment, and Bitcoin trading corporation. 
The interest rate is 5% and the monthly payment is $2684.11.

- Part 2
Suppose Dave pays an extra $1000/month for the first 12 months of the mortgage?

- Part 3
Fix the remaining negation
"""

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0

month = 0

extra_payment_start_month = 61
extra_payment_end_month = 108
extra_payment = 1000

while principal > 0:
    month += 1
    principal = principal * (1+rate/12) - payment
    total_paid = total_paid + payment

    if extra_payment_start_month <= month <= extra_payment_end_month:
        principal -= extra_payment if extra_payment > principal else principal
        total_paid += extra_payment if extra_payment > principal else principal

    print(f"{month} {total_paid:10.2f} {principal:10.2f}")


print(f'Total paid ${total_paid}')
