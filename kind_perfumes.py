kind_perfumes = input("Do you need perfumes for man or woman:\n").lower()

if kind_perfumes == "man":
    man = int(input("How many perfumes do you need:\n"))
    if man == 1:
        print("One Million")
    elif man == 4:
        print("Blue Chanel")
    else:
        print("We don't have this number")

elif kind_perfumes == "woman":
    woman = int(input("How many perfumes do you need:\n"))
    if woman == 2:
        print("One Million")
    elif woman == 3:
        print("Chloe")
    else:
        print("We don't have this number")

else:
    print("Invalid input. Please choose 'man' or 'woman'")