import csv, os

USER_FILE = "files/users.csv"

def signup():
    print("\n------ SIGN UP ------")
    username = input("Username: ").strip()
    password = input("Password: ").strip()
    print("Select role:\n1. Landlord\n2. Tenant")
    role = "landlord" if input("Enter choice: ") == "1" else "tenant"

    os.makedirs("files", exist_ok=True)
    if os.path.exists(USER_FILE):
        with open(USER_FILE, "r") as f:
            for row in csv.reader(f):
                if row and row[0] == username:
                    print("Username already exists.")
                    return
    with open(USER_FILE, "a", newline="") as f:
        csv.writer(f).writerow([username, password, role])
    print(f"Signup successful as {role.title()}!")

def login():
    print("\n------ LOGIN ------")
    username = input("Username: ").strip()
    password = input("Password: ").strip()

    if not os.path.exists(USER_FILE):
        print("No users found.")
        return None, None

    with open(USER_FILE, "r") as f:
        for row in csv.reader(f):
            if row and row[0] == username and row[1] == password:
                print(f"Welcome {username} ({row[2].title()})")
                return username, row[2]
    print("Invalid credentials.")
    return None, None
