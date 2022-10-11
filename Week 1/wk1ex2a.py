import random

comp = random.choice(["steen", "papier", "schaar"])

user = input("Jij kiest: ").lower()

print("Jij koos: ", user)
print("Ik koos: ", comp)

if comp == user:
    print("Gelijkspel...")
elif comp == "steen":
    if user == "papier":
        print("Jij hebt gewonnen....")
    else:
        print("Ik heb gewonnen")
elif comp == "papier":
    if user == "schaar":
        print("Jij hebt gewonnen....")
    else:
        print("Ik heb gewonnen")
elif comp == "schaar":
    if user == "steen":
        print("Jij hebt gewonnen....")
    else:
        print("Ik heb gewonnen")                  