import sys
import os
from datetime import datetime

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))


def add_user(name, last_name, identity_document, email, phone, start_date, end_date, salary):
    
    print("Adding user:", name, last_name, identity_document, email, phone, start_date, end_date, salary)

def add_settlement(indemnity, vacation, severance, severance_interest, service_bonus, withholding_tax, total_payment, user_id):
  
    print("Adding settlement:", indemnity, vacation, severance, severance_interest, service_bonus, withholding_tax, total_payment, user_id)

def query_user(user_id):
    
    print("Querying user with ID:", user_id)

def delete_user(user_id):
    
    print("Deleting user with ID:", user_id)

def delete_settlement(settlement_id):
 
    print("Deleting settlement with ID:", settlement_id)

def main_menu():
    while True:
        print("Select an option:")
        print("1. Add user")
        print("2. Add settlement")
        print("3. Query user")
        print("4. Delete user")
        print("5. Exit")
        print("6. Delete Settlement")

        try:
            option = int(input("Enter the option number: "))
        except ValueError:
            print("Invalid option. Please select a valid option.")
            continue

        if option == 1:
            name = input("Enter the user's first name: ")
            last_name = input("Enter the user's last name: ")
            identity_document = input("Enter the user's identity document: ")
            email = input("Enter the user's email address: ")
            phone = input("Enter the user's phone number: ")
            start_date = input("Enter the user's start date (YYYY-MM-DD): ")
            end_date = input("Enter the user's end date (YYYY-MM-DD): ")
            try:
                salary = float(input("Enter the user's salary: "))
            except ValueError:
                print("Invalid salary. Please enter a numeric value.")
                continue
            add_user(name, last_name, identity_document, email, phone, start_date, end_date, salary)
            print("User successfully added.")

        elif option == 2:
            try:
                indemnity = float(input("Enter the indemnity value: "))
                vacation = float(input("Enter the vacation value: "))
                severance = float(input("Enter the severance value: "))
                severance_interest = float(input("Enter the severance interest value: "))
                service_bonus = float(input("Enter the service bonus value: "))
                withholding_tax = float(input("Enter the withholding tax value: "))
                total_payment = float(input("Enter the total payment value: "))
                user_id = int(input("Enter the user ID: "))
            except ValueError as e:
                print(f"Invalid input: {e}. Please enter valid numeric values.")
                continue

            add_settlement(indemnity, vacation, severance, severance_interest, service_bonus, withholding_tax, total_payment, user_id)
            print("Settlement successfully added.")

        elif option == 3:
            try:
                user_id = int(input("Enter the user ID to query: "))
                query_user(user_id)
            except ValueError:
                print("Invalid user ID. Please enter a numeric value.")

        elif option == 4:
            try:
                user_id = int(input("Enter the user ID to delete: "))
                delete_user(user_id)
                print("User successfully deleted.")
            except ValueError:
                print("Error deleting user. Please check the ID.")

        elif option == 5:
            print("Exiting menu...")
            sys.exit()

        elif option == 6:
            try:
                settlement_id = int(input("Enter the settlement ID to delete: "))
                delete_settlement(settlement_id)
                print("Settlement successfully deleted.")
            except ValueError:
                print("Error deleting settlement. Please check the ID.")

        else:
            print("Invalid option. Please select a valid option.")

if __name__ == "__main__":
    main_menu()
