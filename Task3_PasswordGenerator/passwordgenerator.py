import random
import string

def line():
    print("-" * 65)

def strength_meter(password):
    length = len(password)
    has_lower = any(c.islower() for c in password)
    has_upper = any(c.isupper() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_symbol = any(c in string.punctuation for c in password)

    score = has_lower + has_upper + has_digit + has_symbol

    if length >= 12 and score == 4:
        return "Very Strong 💪"
    elif length >= 10 and score >= 3:
        return "Strong 🔐"
    elif length >= 8 and score >= 2:
        return "Moderate 🙂"
    else:
        return "Weak ❌"


def generate_password(length, choice):
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation

    password_chars = ""
    guaranteed = []

    if choice == "1":  
        password_chars = lowercase + uppercase + digits + symbols
        guaranteed += [
            random.choice(lowercase),
            random.choice(uppercase),
            random.choice(digits),
            random.choice(symbols)
        ]

    elif choice == "2":  
        password_chars = lowercase + uppercase + digits
        guaranteed += [
            random.choice(lowercase),
            random.choice(uppercase),
            random.choice(digits)
        ]

    elif choice == "3":  
        password_chars = lowercase + uppercase
        guaranteed += [
            random.choice(lowercase),
            random.choice(uppercase)
        ]

    elif choice == "4":  
        password_chars = lowercase
        guaranteed.append(random.choice(lowercase))

    else:
        return None

    remaining_length = length - len(guaranteed)

    if remaining_length > 0:
        guaranteed.extend(random.choice(password_chars) for _ in range(remaining_length))

    random.shuffle(guaranteed)
    return "".join(guaranteed)


# ================= MAIN ===================

print("\n" + "=" * 65)
print("                🔐 PASSWORD GENERATOR 🔐")
print("=" * 65 + "\n")


while True:

    # ---- Password Length Input ----
    while True:
        try:
            length = int(input("Enter desired password length: "))
            if length <= 0:
                print("❌ Length must be greater than 0!")
                continue
            break
        except ValueError:
            print("❌ Please enter a valid number!")

    print()
    line()
    print("Select Password Complexity (Recommended First):\n")
    print("1️⃣  Strong (Letters + Numbers + Symbols)  ✅ Recommended")
    print("2️⃣  Letters + Numbers")
    print("3️⃣  Lowercase + Uppercase")
    print("4️⃣  Only Lowercase\n")

    choice = input("Enter your choice (1/2/3/4): ")

    if choice not in ["1", "2", "3", "4"]:
        print("\n❌ Invalid choice. Try again.\n")
        continue

    # ===== Inner Loop (Generate Again / Change / Exit) =====
    while True:
        print()
        line()
        print("Generated Password Details:\n")

        password = generate_password(length, choice)

        print(f"🔑 Password          :  {password}")
        print(f"📊 Password Strength :  {strength_meter(password)}")

        print()
        line()
        print("What do you want to do next?\n")
        print("1️⃣  Generate NEXT Password (same requirements)")
        print("2️⃣  Change Password Requirements")
        print("3️⃣  Exit")

        option = input("\nEnter your choice: ")

        if option == "1":
            continue
        elif option == "2":
            break
        elif option == "3":
            print()
            line()
            print("✅ Thank you for using Password Generator! 😊")
            line()
            exit()
        else:
            print("\n❌ Invalid option. Try again.\n")
