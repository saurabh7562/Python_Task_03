import random
import string

while True:
    # ask for password length
    length = int(input("\nEnter password length: "))

    print("\nChoose password type:")
    print("1. Only letters")
    print("2. Letters + numbers")
    print("3. Strong (letters + numbers + symbols)")
    print("0. Exit")

    choice = int(input("Enter your choice (0/1/2/3): "))

    # exit option
    if choice == 0:
        print("Goodbye ")
        break

    if choice == 1:
        password_characters = string.ascii_letters
        password = "".join(random.choice(password_characters) for _ in range(length))

    elif choice == 2:
        password_characters = string.ascii_letters + string.digits

        password = [
            random.choice(string.ascii_letters),
            random.choice(string.digits)
        ]
        password += [random.choice(password_characters) for _ in range(length - 2)]
        random.shuffle(password)
        password = "".join(password)

    elif choice == 3:
        password_characters = string.ascii_letters + string.digits + string.punctuation

        password = [
            random.choice(string.ascii_lowercase),
            random.choice(string.ascii_uppercase),
            random.choice(string.digits),
            random.choice(string.punctuation)
        ]
        password += [random.choice(password_characters) for _ in range(length - 4)]
        random.shuffle(password)
        password = "".join(password)

    else:
        print("Invalid choice — try again!")
        continue

    print("\nYour password is:", password)
