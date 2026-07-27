# ==========================================
# Project : Contact Book
# Author : Pooja Singh
# GitHub : Pooja0599
# ==========================================

contacts = {}

print("=" * 50)
print("         CONTACT BOOK SYSTEM")
print("=" * 50)

while True:

    print("\n1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Exit")

    choice = input("\nEnter Your Choice : ")

    # ==========================================
    # Add Contact
    # ==========================================

    if choice == "1":

        name = input("Enter Name : ")
        phone = input("Enter Phone Number : ")

        contacts[name] = phone

        print("Contact Added Successfully.")

    # ==========================================
    # View Contacts
    # ==========================================

    elif choice == "2":

        if len(contacts) == 0:
            print("No Contacts Found.")

        else:
            print("\n----- Contact List -----")

            for name, phone in contacts.items():
                print(name, ":", phone)

    # ==========================================
    # Search Contact
    # ==========================================

    elif choice == "3":

        name = input("Enter Name to Search : ")

        if name in contacts:
            print("Phone Number :", contacts[name])

        else:
            print("Contact Not Found.")

    # ==========================================
    # Delete Contact
    # ==========================================

    elif choice == "4":

        name = input("Enter Name to Delete : ")

        if name in contacts:
            del contacts[name]
            print("Contact Deleted Successfully.")

        else:
            print("Contact Not Found.")

    # ==========================================
    # Exit
    # ==========================================

    elif choice == "5":

        print("\nThank You for Using Contact Book.")
        break

    # ==========================================
    # Invalid Choice
    # ==========================================

    else:

        print("Invalid Choice. Please Try Again.")