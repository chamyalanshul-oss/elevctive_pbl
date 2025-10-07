import csv, os

PAYMENT_FILE = "files/payments.csv"
EXPENSE_FILE = "files/expenses.csv"

def summary_report():
    rent_total = 0
    exp_total = 0
    if os.path.exists(PAYMENT_FILE):
        with open(PAYMENT_FILE, "r") as f:
            for r in csv.reader(f):
                if r: rent_total += float(r[1])
    if os.path.exists(EXPENSE_FILE):
        with open(EXPENSE_FILE, "r") as f:
            for r in csv.reader(f):
                if r: exp_total += float(r[1])
    print(f"\nTotal Rent Collected : ₹{rent_total}")
    print(f"Total Expenses       : ₹{exp_total}")
    print(f"Net Income           : ₹{rent_total - exp_total}")
