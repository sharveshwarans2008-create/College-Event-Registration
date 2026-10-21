from events import view_events
from registration import register_student, view_registrations

while True:
    print("\n===== College Event Registration =====")
    print("1. View Events")
    print("2. Register for an Event")
    print("3. View Registrations")
    print("4. Exit")

    choice = input("Enter your choice: ")

    try:
        if choice == "1":
            view_events()
        elif choice == "2":
            register_student()
        elif choice == "3":
            view_registrations()
        elif choice == "4":
            print("Thank you!")
            break
        else:
            print("Invalid choice. Try again.")

    except Exception as error:
        print("An error occurred:", error)
