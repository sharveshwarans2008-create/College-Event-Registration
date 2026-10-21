from events import get_connection

def register_student():
    name = input("Enter student name: ").strip()
    roll_no = input("Enter roll number: ").strip()

    if not name or not roll_no:
        print("Name and roll number cannot be empty.")
        return

    try:
        event_id = int(input("Enter event ID: "))
    except ValueError:
        print("Enter a valid numeric event ID.")
        return

    con = get_connection()
    cur = con.cursor()

    try:
        cur.execute(
            "SELECT event_id FROM events WHERE event_id = %s",
            (event_id,)
        )

        if cur.fetchone() is None:
            print("Invalid event ID.")
            return

        cur.execute("""
            INSERT INTO registrations
                (student_name, roll_no, event_id)
            VALUES (%s, %s, %s)
        """, (name, roll_no, event_id))

        con.commit()
        print("Registration successful!")

    except Exception as error:
        con.rollback()
        print("Registration failed:", error)

    finally:
        cur.close()
        con.close()


def view_registrations():
    con = get_connection()
    cur = con.cursor()

    try:
        cur.execute("""
            SELECT r.registration_id,
                   r.student_name,
                   r.roll_no,
                   e.event_name,
                   r.registration_date
            FROM registrations r
            JOIN events e ON r.event_id = e.event_id
            ORDER BY r.registration_id
        """)

        print("\n--- Student Registrations ---")

        rows = cur.fetchall()

        if not rows:
            print("No registrations found.")
            return

        for row in rows:
            print(
                f"Registration ID: {row[0]} | "
                f"Name: {row[1]} | Roll No: {row[2]} | "
                f"Event: {row[3]} | Registered: {row[4]}"
            )

    finally:
        cur.close()
        con.close()
