def compute_trip(miles, gallons):
    mpg = miles / gallons
    gas_cost = gallons * 3.00
    return mpg, gas_cost

trip_count = 0
total_miles = 0
total_cost = 0

while True:
    again = input("Enter a trip? (Yes/No): ").lower()
    if again != "yes":
        break

    city = input("Enter destination city: ")
    miles = float(input("Enter miles traveled: "))
    gallons = float(input("Enter gallons used: "))

    mpg, gas_cost = compute_trip(miles, gallons)

    trip_count += 1
    total_miles += miles
    total_cost += gas_cost

    print(f"City: {city}")
    print(f"Miles: {miles}")
    print(f"MPG: {mpg:.2f}")
    print(f"Gas Cost: ${gas_cost:.2f}")
    print()

print(f"Number of trips: {trip_count}")
print(f"Total miles: {total_miles}")
print(f"Total gas cost: ${total_cost:.2f}")
