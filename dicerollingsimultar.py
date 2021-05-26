import random

print("Welcome to dice rolling simultar")
input("Press Enter to continue")
p1name=input("Enter Player 1 Name: ")
p2name=input("Enter Player 2 Name: ")
print(f"Rolling rice for {p1name}...")
p1=random.randint(1,6)
print(p1)
input(f"Press Enter to roll dice for {p2name}")
print(f"Rolling rice for {p2name}...")
p2=random.randint(1,6)
print(p2)
if p1>p2:
    print(f"{p1name} won")
elif p1==p2:
    print("It's a draw")
else:
    print(f"{p2name} won")