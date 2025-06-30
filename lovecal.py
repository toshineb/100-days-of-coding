def Flames(name1, name2):
    # Combine the names
    namestr = name1 + name2

    # Remove common letters
    for c in set(namestr):  # Use set to avoid redundant replacements
        if namestr.count(c) != 1:
            namestr = namestr.replace(c, "")

    # Define FLAMES meanings
    print("FLAMES....")
    print("F = Friend \nL = Love \nA = Affection \nM = Marriage \nE = Enemy \nS = Siblings \n\n")

    # Determine the FLAMES result
    number = len(namestr) % 6
    rel = ""

    if number == 1:
        rel = "Friends"
    elif number == 2:
        rel = "Love"
    elif number == 3:
        rel = "Affection"
    elif number == 4:
        rel = "Marriage"
    elif number == 5:
        rel = "Enemy"
    elif number == 0:
        rel = "Siblings"

    return rel


# Get input from users
n1 = input("Enter your name: ").strip().upper()
n2 = input("Enter the name of your crush: ").strip().upper()

# Call the function and print the result
print(f"Your Relationship is: {Flames(n1, n2)}")
