from decimal import Decimal, InvalidOperation


def parse_money(value, field_name, *, allow_zero=True):
    """Convert input to a non-negative Decimal amount."""
    try:
        amount = Decimal(str(value).strip())
    except (InvalidOperation, ValueError):
        raise ValueError(f"{field_name} must be a valid number.")

    if not amount.is_finite():
        raise ValueError(f"{field_name} must be a finite number.")
    if amount < 0 or (not allow_zero and amount == 0):
        qualifier = "greater than zero" if not allow_zero else "zero or greater"
        raise ValueError(f"{field_name} must be {qualifier}.")

    return amount


def monthly_budget_check(budget, spent):
    budget = parse_money(budget, "Monthly budget")
    spent = parse_money(spent, "Amount spent")

    remaining = budget - spent
    if remaining >= 0:
        return f"Within budget. Remaining: ${remaining:.2f}"
    return f"Over budget by: ${abs(remaining):.2f}"


def payment_amount_check(amount_due, payment):
    amount_due = parse_money(amount_due, "Amount due", allow_zero=False)
    payment = parse_money(payment, "Payment amount", allow_zero=False)

    if payment > amount_due:
        raise ValueError(f"Payment cannot exceed the amount due (${amount_due:.2f}).")

    return f"Payment amount is valid: ${payment:.2f}"


def run_option(option):
    try:
        if option == "1":
            budget = input("Monthly budget: $")
            spent = input("Amount spent this month: $")
            print(monthly_budget_check(budget, spent))
        elif option == "2":
            due = input("Amount due: $")
            payment = input("Payment amount: $")
            print(payment_amount_check(due, payment))
        else:
            print("Please choose option 1 or 2.")
    except ValueError as error:
        print(f"Invalid input: {error}")


if __name__ == "__main__":
    # Test prints
    print("Option 1 test:", monthly_budget_check("1000", "725.50"))
    print("Option 1 over-budget test:", monthly_budget_check("500", "550"))
    print("Option 2 test:", payment_amount_check("250", "100"))

    try:
        payment_amount_check("250", "300")
    except ValueError as error:
        print("Option 2 validation test:", error)

    print("\n1) Monthly budget check\n2) Payment amount check")
    run_option(input("Choose an option: ").strip())
