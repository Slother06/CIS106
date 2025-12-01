def compute_tuition(credits, code):
    if code == "I":
        return credits * 250
    elif code == "O":
        return credits * 550
    else:
        return 0

total_tuition = 0

while True:
    again = input("Enter a student? (Yes/No): ").lower()
    if again != "yes":
        break

    name = input("Enter student last name: ")
    credits = float(input("Enter credit hours: "))
    code = input("Enter district code (I or O): ").upper()

    tuition = compute_tuition(credits, code)
    total_tuition += tuition

    print(f"Student: {name}")
    print(f"Tuition Owed: ${tuition:.2f}")
    print()

print(f"Total tuition for all students: ${total_tuition:.2f}")
