import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="YOUR_MYSQL_PASSWORD",
        database="college_event_db"
    )

def view_events():
    con = get_connection()
    cur = con.cursor()

    try:
        cur.execute(
            "SELECT event_id, event_name, event_date, venue FROM events"
        )

        print("\n--- Available College Events ---")

        for event in cur.fetchall():
            print(
                f"ID: {event[0]} | Name: {event[1]} | "
                f"Date: {event[2]} | Venue: {event[3]}"
            )
    finally:
        cur.close()
        con.close()
