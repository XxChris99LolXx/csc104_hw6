def payment_periods(years):
    return years * 12

def monthly_interest_rate(annual_rate_percent):
    return annual_rate_percent / 100 / 12

def monthly_loan_payment(loan_amount, annual_rate_percent, years):
    n = payment_periods(years)
    r = monthly_interest_rate(annual_rate_percent)
    payment = loan_amount * r / (1 - (1 + r) ** (-n))
    return payment

if __name__ == "__main__":
    loan_amount = float(input("Loan amount: "))
    annual_rate_percent = float(input("Annual percent: "))
    years = int(input("Years: "))
    payment = monthly_loan_payment(loan_amount, annual_rate_percent, years)
    print(f"${payment:.2f}")