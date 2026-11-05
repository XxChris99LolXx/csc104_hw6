
# Data nouns: amount, goal, rate, years, monthly_payment, monthly_savings
# Action verbs: validate, convert, calculate, display, check, test

def is_positive_amount(amount):
    """Return True if a numeric amount is greater than zero."""
    if amount > 0:
        return True
    else:
        return False

def is_positive_rate(rate_percent):
    """Return True if numeric annual percentage is above zero."""
    if rate_percent > 0:
        return True
    else:
        return False

def is_valid_years(years):
    """Return True if numeric years are positive and whole."""
    if years <= 0:
        return False
    elif years % 1 != 0:
        return False
    else:
        return True

# --- Existing Helpers ---
def payment_periods(years):
    return int(years) * 12

def monthly_interest_rate(rate_percent):
    return (rate_percent / 100) / 12

def monthly_loan_payment(amount, rate, years):
    i = monthly_interest_rate(rate)
    n = payment_periods(years)
    return amount * (i * (1 + i)**n) / ((1 + i)**n - 1)

def monthly_savings_payment(goal, rate, years):
    i = monthly_interest_rate(rate)
    n = payment_periods(years)
    return goal * i / ((1 + i)**n - 1)


# --- Step 3: Direct Validator Tests ---
print("--- Validator Direct Tests ---")
print("is_positive_amount (12000, 0, -100):", is_positive_amount(12000), is_positive_amount(0), is_positive_amount(-100))
print("is_positive_rate (6.0, 0, -1):", is_positive_rate(6.0), is_positive_rate(0), is_positive_rate(-1))
print("is_valid_years (5.0, 0, 2.25):", is_valid_years(5.0), is_valid_years(0), is_valid_years(2.25))
# Note: positive 2.5 fails this contract because 2.5 % 1 != 0 (it is not a whole number).


# --- Step 4: Integrated Loan and Savings Programs with Gates ---
print("\n--- Loan Input Program ---")
raw_loan_amount = float(input("Enter loan amount: "))
raw_loan_rate = float(input("Enter annual interest rate (e.g., 6 for 6%): "))
raw_loan_years = float(input("Enter loan term in years: "))

if not is_positive_amount(raw_loan_amount):
    print("Amount or goal error")
elif not is_positive_rate(raw_loan_rate):
    print("Rate error")
elif not is_valid_years(raw_loan_years):
    print("Years error")
else:
    # Reaching else means all checks passed
    loan_years_int = int(raw_loan_years)
    payment = monthly_loan_payment(raw_loan_amount, raw_loan_rate, loan_years_int)
    print(f"Loan ${payment:.2f}")


print("\n--- Savings Input Program ---")
raw_savings_goal = float(input("Enter savings goal: "))
raw_savings_rate = float(input("Enter annual interest rate (e.g., 6 for 6%): "))
raw_savings_years = float(input("Enter savings term in years: "))

if not is_positive_amount(raw_savings_goal):
    print("Amount or goal error")
elif not is_positive_rate(raw_savings_rate):
    print("Rate error")
elif not is_valid_years(raw_savings_years):
    print("Years error")
else:
    # Zero years would be unsafe for original formulas because payment_periods(0) causes division by zero
    savings_years_int = int(raw_savings_years)
    deposit = monthly_savings_payment(raw_savings_goal, raw_savings_rate, savings_years_int)
    print(f"Savings ${deposit:.2f}")
