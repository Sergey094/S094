import sys
import os

# добавляем корневую папку проекта
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from phonebook.db import *


def menu():
    while True:
        print("\n--- PHONEBOOK MENU ---")
        print("1. Create table")
        print("2. Insert contact")
        print("3. Insert from CSV")
        print("4. Show all contacts")
        print("5. Search")
        print("6. Update contact")
        print("7. Delete contact")
        print("0. Exit")

        choice = input("Choose: ")

        if choice == "1":
            create_table()
            print("Table created")

        elif choice == "2":
            name = input("Name: ")
            phone = input("Phone: ")
            insert_contact(name, phone)

        elif choice == "3":
            filename = input("CSV filename: ")
            insert_from_csv(filename)

        elif choice == "4":
            contacts = show_all()
            for c in contacts:
                print(f"ID: {c[0]}, Name: {c[1]}, Phone: {c[2]}")

        elif choice == "5":
            name = input("Search name: ")
            results = search(name)
            for r in results:
                print(r)

        elif choice == "6":
            old = input("Old name: ")
            new = input("New name: ")
            phone = input("New phone: ")
            update_contact(old, new, phone)

        elif choice == "7":
            name = input("Delete name: ")
            delete_contact(name)

        elif choice == "0":
            break

        else:
            print("Invalid choice")


if __name__ == "__main__":
    menu()