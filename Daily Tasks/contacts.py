# Simple Contact Book (using dictionary)

contacts={}

while True:

    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Delete Contact")

    choice=input("Enter your choice(1-3):")

    if choice=="1":

        name=input("Enter name:")
        phone=input('Enter number:')


        if name in contacts:

            contacts[name].append(phone)

        else:

            contacts[name]=[phone]

        print("contact added successfully for",name)
    elif choice=="2":

        if contacts:

            for name,numbers in contacts.items():

                print(f"{name}:{phone}")

        else:

            print("No contacts found")

    elif choice=='3':

        name=input("ENter name to delete:")

        if name in contacts:
            
            del contacts[name]
            print("Contact deleted successfully")
        else:

            print("Contact not found")

    else:

        print("Invalid choice. ENter between 1-3")

#name as key and number as list of values