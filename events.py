import mysql.connector


def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="SHARVESH101108",
        database="college_event_db"
    )


def view_events():
    connection = get_connection()
    cursor = connection.cursor()

    try:
        cursor.execute(
            "SELECT event_id, event_name, event_date, venue FROM events"
        )
        events = cursor.fetchall()

        print("\n--- Available College Events ---")

        if not events:
            print("No events available.")
        else:
            for event in events:
                print(
                    f"ID: {event[0]} | Name: {event[1]} | "
                    f"Date: {event[2]} | Venue: {event[3]}"
                )
    finally:
        cursor.close()
        connection.close()