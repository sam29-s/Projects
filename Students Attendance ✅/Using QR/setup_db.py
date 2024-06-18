import sqlite3

def setup_database():
    conn = sqlite3.connect('attendance.db')
    cursor = conn.cursor()

    # Create the attendees table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS attendees (
        id INTEGER PRIMARY KEY,
        name TEXT,
        qr_code TEXT UNIQUE
    )
    ''')

    # Create the attendance table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS attendance (
        id INTEGER PRIMARY KEY,
        attendee_id INTEGER,
        timestamp DATETIME,
        FOREIGN KEY (attendee_id) REFERENCES attendees (id)
    )
    ''')

    # Prompt user to input attendees
    while True:
        name = input("Enter attendee name (or 'q' to quit): ")
        if name.lower() == 'q':
            break
        qr_code = input(f"Enter QR code for {name}: ")

        # Insert attendee into database
        cursor.execute("INSERT OR IGNORE INTO attendees (name, qr_code) VALUES (?, ?)", (name, qr_code))

    conn.commit()
    print("Database setup complete.")

    conn.close()

if __name__ == "__main__":
    setup_database()
