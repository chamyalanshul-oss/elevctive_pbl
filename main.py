from auth import signup, login
from landlord import landlord_menu
from tenant import tenant_menu

def main_menu():
    while True:
        print("\n====== HOUSE RENT SYSTEM ======")
        print("1. Login")
        print("2. Sign Up")
        print("3. Exit")
        ch = input("Enter choice: ")
        if ch == "1":
            username, role = login()
            if role == "landlord": landlord_menu()
            elif role == "tenant": tenant_menu(username)
        elif ch == "2": signup()
        elif ch == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main_menu()
