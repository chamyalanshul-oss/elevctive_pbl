import csv, os

TENANT_FILE = "files/tenants.csv"
PAYMENT_FILE = "files/payments.csv"

def view_my_details(username):
    if not os.path.exists(TENANT_FILE):
        print("No tenant data yet.")
        return
    found = False
    with open(TENANT_FILE, "r") as f:
        for row in csv.reader(f):
            if row and row[1].lower() == username.lower():
                print(f"Tenant Info: ID:{row[0]} | Name:{row[1]} | Rent:₹{row[2]} | Due:{row[3]}")
                found = True
    if not found:
        print("No record found for you.")

def view_my_payments(username):
    if not os.path.exists(PAYMENT_FILE):
        print("No payments yet.")
        return
    total = 0
    with open(PAYMENT_FILE, "r") as f:
        for row in csv.reader(f):
            if row and (row[0].lower() == username.lower() or row[0] == username):
                print(f"Date:{row[2]} | Amount:₹{row[1]} | Status:{row[3]}")
                total += float(row[1])
    print(f"Total Paid: ₹{total}")

def tenant_menu(username):
    while True:
        print("\n====== TENANT MENU ======")
        print("1. View My Details")
        print("2. View My Payments")
        print("3. Logout")
        ch = input("Enter choice: ")
        if ch == "1": view_my_details(username)
        elif ch == "2": view_my_payments(username)
        elif ch == "3": break
        else: print("Invalid option.")
