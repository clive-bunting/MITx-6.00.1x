balance = 4842 # the outstanding balance on the credit card
annualInterestRate = 0.2 # annual interest rate as a decimal
monthlyPaymentRate = 0.04 # minimum monthly payment rate as a decimal

monthlyInterestRate = annualInterestRate / 12.0
totalPaid = 0.0

for month in range(1,13):
    minimumMonthlyPayment = monthlyPaymentRate * balance
    totalPaid += minimumMonthlyPayment 
    balance -= minimumMonthlyPayment
    balance += (monthlyInterestRate * balance)
    
    print 'Month:',
    print month
    print 'Minimum monthly payment:',
    print round(minimumMonthlyPayment , 2)
    print 'Remaining balance:',
    print round(balance, 2)

print 'Total paid:',
print round(totalPaid, 2)
print 'Remaining balance:',
print round(balance, 2)