man_perfumes = {
    1: "One Million",
    4: "Blue Chanel"
}

woman_perfumes = {
    2: "One Million",
    3: "Chloe"
}

def get_perfume(kind, number):
    if kind == "man":
        return man_perfumes.get(number, "We don't have this number")
    elif kind == "woman":
        return woman_perfumes.get(number, "We don't have this number")
    else:
        return "Invalid input. Please choose 'man' or 'woman'"

# تأكد من تشغيل هذا الجزء أولاً
kind = input("Do you need perfumes for man or woman:\n").lower()

if kind in ["man", "woman"]:
    try:
        number = int(input("How many perfumes do you need:\n"))
        print(get_perfume(kind, number))
    except ValueError:
        print("Please enter a valid number.")
else:
    print("Invalid input. Please choose 'man' or 'woman'")