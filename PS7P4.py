def compute_pay(code, hours):
    if code == "L":
        rate = 25
    elif code == "A":
        rate = 30
    elif code == "J":
        rate = 50
    else:
        rate = 0

    if hours > 40:
        overtime = (hours - 40) * (rate * 1.5)
        gross = (40 * rate) + overtime
    else:
        gross = hours * rate

    return rate, gross

total_gross = 0

while True:
    again = input("Enter an employee? (Yes/No): ").lower()
    if again != "yes":
        break

    last = input("Enter employee last name: ")
    code = input("Enter job code (L, A, J): ").upper()
    hours = float(input("Enter hours worked: "))

    rate, gross = compute_pay(code, hours)
    total_gross += gross

    print(f"Employee: {last}")
    print(f"Hours: {hours}")
    print(f"Pay Rate: ${rate:.2f}")
    print(f"Gross Pay: ${gross:.2f}")
    print()

print(f"Total gross pay for all employees: ${total_gross:.2f}")
