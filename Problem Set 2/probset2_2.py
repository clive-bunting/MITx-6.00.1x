balance = 3926 # the outstanding balance on the credit card
annualInterestRate = 0.2 # annual interest rate as a decimal

monthlyInterestRate = annualInterestRate / 12.0

for monthlyPayment in range (10, balance, 10):
    balanceToPay = balance
    for month in range(1,13):
        balanceToPay -= monthlyPayment
        balanceToPay += (monthlyInterestRate * balanceToPay)
    if balanceToPay <= 0.0:
        print 'Lowest Payment:',
        print monthlyPayment
        break
