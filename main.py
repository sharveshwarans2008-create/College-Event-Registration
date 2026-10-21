
from events import view_events
from registration import register_student, view_registrations


def main():
    while True:
        print("\n===== COLLEGE EVENT REGISTRATION SYSTEM =====")
        print("1. View Events")
        print("2. Register for an Event")
        print("3. View Registrations")
        print("4. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            view_events()

        elif choice == "2":
            register_student()

        elif choice == "3":
            view_registrations()

        elif choice == "4":
            print("Thank you for using the application!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
