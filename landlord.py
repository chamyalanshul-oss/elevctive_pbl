import csv, os
from datetime import datetime

TENANT_FILE = "files/tenants.csv"
PAYMENT_FILE = "files/payments.csv"
EXPENSE_FILE = "files/expenses.csv"

def add_tenant():
    tenant_id = input("Tenant ID: ")
    name = input("Tenant Name: ")
    rent = input("Monthly Rent (₹): ")
    due = input("Due Date (DD/MM/YYYY): ")
    contact = input("Contact No: ")
    with open(TENANT_FILE, "a", newline="") as f:
        csv.writer(f).writerow([tenant_id, name, rent, due, contact])
    print("Tenant added successfully.")

def view_tenants():
    if not os.path.exists(TENANT_FILE):
        print("No tenant records.")
        return
    print("\n------ TENANT LIST ------")
    with open(TENANT_FILE, "r") as f:
        for row in csv.reader(f):
            if row:
                print(f"ID:{row[0]} | Name:{row[1]} | Rent:₹{row[2]} | Due:{row[3]} | Contact:{row[4]}")

def record_payment():
    tenant_id = input("Tenant ID: ").strip()
    rent_amount = None
    if os.path.exists(TENANT_FILE):
        with open(TENANT_FILE, "r") as f:
            for row in csv.reader(f):
                if row and row[0] == tenant_id:
                    rent_amount = float(row[2])
                    break
    if rent_amount is None:
        print("Tenant not found.")
        return
    date = datetime.now().strftime("%d/%m/%Y")
    with open(PAYMENT_FILE, "a", newline="") as f:
        csv.writer(f).writerow([tenant_id, rent_amount, date, "Paid"])
    print(f"Payment of ₹{rent_amount} recorded for {tenant_id}.")

def add_expense():
    title = input("Expense Title: ")
    amt = float(input("Amount (₹): "))
    date = datetime.now().strftime("%d/%m/%Y")
    with open(EXPENSE_FILE, "a", newline="") as f:
        csv.writer(f).writerow([title, amt, date])
    print("Expense added.")

def landlord_menu():
    while True:
        print("\n====== LANDLORD MENU ======")
        print("1. Add Tenant")
        print("2. View Tenants")
        print("3. Record Payment")
        print("4. Add Expense")
        print("5. Summary Report")
        print("6. Logout")
        ch = input("Enter choice: ")
        if ch == "1": add_tenant()
        elif ch == "2": view_tenants()
        elif ch == "3": record_payment()
        elif ch == "4": add_expense()
        elif ch == "5": from report import summary_report; summary_report()
        elif ch == "6": break
        else: print("Invalid option.")
