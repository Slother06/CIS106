def compute_total(qty, price):
    total = qty * price
    if total > 10000:
        total *= 0.90  # 10% discount
    return total

overall_total = 0

while True:
    again = input("Do you want to run the program? (Yes/No): ").lower()
    if again != "yes":
        break

    qty = float(input("Enter quantity: "))
    price = float(input("Enter price: "))

    total = compute_total(qty, price)
    overall_total += total

    print(f"Quantity: {qty}")
    print(f"Price: ${price:.2f}")
    print(f"Total after discount: ${total:.2f}")
    print()

print(f"Extended price (sum of all totals): ${overall_total:.2f}")
