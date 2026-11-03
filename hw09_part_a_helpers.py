def payment_periods(years):
    return years * 12

def monthly_interest_rate(annual_rate_percent):
    return (annual_rate_percent / 100) / 12

print("5 years ->", payment_periods(5))
print("6 percent ->", monthly_interest_rate(6))

