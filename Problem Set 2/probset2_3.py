balance = 999999 # the outstanding balance on the credit card
annualInterestRate = 0.18 # annual interest rate as a decimal

monthlyInterestRate = annualInterestRate / 12.0

monthlyPaymentLowerBound = balance / 12
monthlyPaymentUpperBound = (balance * (1.0 + monthlyInterestRate)**12) / 12.0
epsilon = 0.01

def CalculateRemainingBalance(monthlyPayment, balance, monthlyInterestRate):
    for month in range(1,13):
        balance -= monthlyPayment
        balance += (monthlyInterestRate * balance)
    return balance

monthlyPayment = (monthlyPaymentUpperBound + monthlyPaymentLowerBound) / 2.0
remainingBalance = CalculateRemainingBalance(monthlyPayment, balance, monthlyInterestRate)

while abs(remainingBalance) > epsilon:
    if remainingBalance > 0.0:
        monthlyPaymentLowerBound =  monthlyPayment
    else:
        monthlyPaymentUpperBound = monthlyPayment
    monthlyPayment = (monthlyPaymentUpperBound + monthlyPaymentLowerBound) / 2.0  
    remainingBalance = CalculateRemainingBalance(monthlyPayment, balance, monthlyInterestRate)

print 'Lowest Payment:',
print round(monthlyPayment, 2)
