import json, random
from classes import Customer, BankAccount


def fetchCustomers():
    try:
        with open("./data.json", "rt", encoding="utf-8") as file:
            data = json.load(file)
            customers = data["customers"]

        for customer in customers:
            print(f"{customer['firstName']} {customer['lastName']}")

        print("\n-----------------------------\n")

    except FileNotFoundError:
        print("The file data.json was not found.")
        print("\n-----------------------------\n")

    except json.JSONDecodeError:
        print("Error decoding JSON from the file.")
        print("\n-----------------------------\n")


def addCustomer(firstName, lastName):
    try:
        with open("./data.json", "rt", encoding="utf-8") as file:
            data = json.load(file)
            customers = data["customers"]

        customer = Customer(firstName, lastName)

        new_customer = {
            "firstName": customer.firstName,
            "lastName": customer.lastName,
            "accountNumber": customer.bank_account.account_number,
            "balance": customer.bank_account.balance,
        }

        customers.append(new_customer)

        with open("./data.json", "wt", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

        print(f"Customer {customer.firstName} {customer.lastName} added successfully.")
        print("\n-----------------------------\n")

    except FileNotFoundError:
        print("The file data.json was not found.")
        print("\n-----------------------------\n")

    except json.JSONDecodeError:
        print("Error decoding JSON from the file.")
        print("\n-----------------------------\n")


def updateCustomer(account_number, firstName, lastName):
    try:
        with open("./data.json", "rt", encoding="utf-8") as file:
            data = json.load(file)
            customers = data["customers"]

        customerFound = False

        for customer in customers:
            if account_number == customer["accountNumber"]:
                customer["firstName"] = firstName
                customer["lastName"] = lastName
                customerFound = True
                print(f"Customer {firstName} {lastName} updated successfully.")
                print("\n-----------------------------\n")
                break

        if customerFound:
            with open("./data.json", "wt", encoding="utf-8") as file:
                json.dump(data, file, ensure_ascii=False, indent=4)

    except FileNotFoundError:
        print("The file data.json was not found.")
        print("\n-----------------------------\n")

    except json.JSONDecodeError:
        print("Error decoding JSON from the file.")
        print("\n-----------------------------\n")


def deleteCustomer(account_number):
    try:
        with open("./data.json", "rt", encoding="utf-8") as file:
            data = json.load(file)
            customers = data["customers"]

        customerFound = False

        for customer in customers:
            if account_number == customer["accountNumber"]:
                customers.remove(customer)
                customerFound = True

                print(
                    f"Customer {customer['firstName']} {customer['lastName']} deleted successfully."
                )
                print("\n-----------------------------\n")
                break

        if not customerFound:
            print(f"Customer with account number {account_number} not found.")
            return

        with open("./data.json", "wt", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

    except FileNotFoundError:
        print("The file data.json was not found.")
        print("\n-----------------------------\n")

    except json.JSONDecodeError:
        print("Error decoding JSON from the file.")
        print("\n-----------------------------\n")


deleteCustomer(601999)

# TODO - Enhance the parameters of the functions.
