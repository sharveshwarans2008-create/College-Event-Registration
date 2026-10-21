
from events import get_connection


def register_student():
    connection = get_connection()
    cursor = connection.cursor()

    try:
        print("\n--- Student Event Registration ---")

        name = input("Enter student name: ").strip()
        roll_no = input("Enter roll number: ").strip()

        if not name or not roll_no:
            print("Name and roll number cannot be empty.")
            return

        cursor.execute("SELECT event_id, event_name FROM events")
        events = cursor.fetchall()

        if not events:
            print("No events are available.")
            return

        print("\nAvailable Events:")
        for event in events:
            print(f"{event[0]}. {event[1]}")

        try:
            event_id = int(input("Enter event ID: "))
        except ValueError:
            print("Please enter a valid numeric event ID.")
            return

        cursor.execute(
            "SELECT event_id FROM events WHERE event_id = %s",
            (event_id,)
        )

        if cursor.fetchone() is None:
            print("Invalid event ID.")
            return

        cursor.execute(
            """
            INSERT INTO registrations (student_name, roll_no, event_id)
            VALUES (%s, %s, %s)
            """,
            (name, roll_no, event_id)
        )

        connection.commit()
        print("Registration successful!")

    except Exception as error:
        connection.rollback()
        print("Registration failed:", error)

    finally:
        cursor.close()
        connection.close()


def view_registrations():
    connection = get_connection()
    cursor = connection.cursor()

    try:
        cursor.execute(
            """
            SELECT r.registration_id, r.student_name, r.roll_no,
                   e.event_name, r.registration_date
            FROM registrations r
            JOIN events e ON r.event_id = e.event_id
            ORDER BY r.registration_id
            """
        )

        records = cursor.fetchall()

        print("\n--- Student Registrations ---")

        if not records:
            print("No registrations found.")
        else:
            for record in records:
                print(
                    f"ID: {record[0]} | Name: {record[1]} | "
                    f"Roll No: {record[2]} | Event: {record[3]} | "
                    f"Date: {record[4]}"
                )

    except Exception as error:
        print("Could not retrieve registrations:", error)

    finally:
        cursor.close()
        connection.close()
