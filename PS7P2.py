def batting_average(hits, at_bats):
    if at_bats == 0:
        return 0
    return hits / at_bats

player_count = 0

while True:
    again = input("Do you want to enter a player? (Yes/No): ").lower()
    if again != "yes":
        break

    last = input("Enter player's last name: ")
    hits = float(input("Enter number of hits: "))
    at_bats = float(input("Enter number of at bats: "))

    avg = batting_average(hits, at_bats)
    player_count += 1

    print(f"Player: {last}, Batting Average: {avg:.3f}")
    print()

print(f"Number of players entered: {player_count}")
