import cv2
import os  # accessing the os functions (provides functions for interacting with the operating system)
from pyzbar.pyzbar import decode
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Global list to store attendance records
attendance_records = []

def mainMenu():
    print()
    print(10 * "*", "WELCOME MENU", 10 * "*")
    print("[1] Scan Attendance")
    print("[2] Auto Mail")
    print("[3] Quit")

    while True:
        try:
            choice = int(input("Enter Choice: "))

            if choice == 1:
                scan_attendance()
                break
            elif choice == 2:
                auto_mail()
                break
            elif choice == 3:
                print("Thank You")
                break
            else:
                print("Invalid Choice. Enter 1-3")
        except ValueError:
            print("Invalid Choice. Enter 1-3\n Try Again")
    exit

def scan_attendance():
    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()

        if ret:
            decoded_objects = decode(frame)
            for obj in decoded_objects:
                qr_data = obj.data.decode('utf-8').strip()  # Ensure no leading/trailing spaces

                print(f"QR Code detected: {qr_data}")

                # Example validation based on content
                if is_valid_qr(qr_data):
                    print("Valid QR code")
                    # Add attendance record
                    record_attendance(qr_data)
                else:
                    print("Invalid QR code")

            cv2.imshow('frame', frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    cap.release()
    cv2.destroyAllWindows()

def is_valid_qr(qr_data):
    # Example validation function, adjust as per your requirements
    valid_names = ["Arun Kumar", "Sam", "maddy"]  # List of valid names
    return qr_data in valid_names

def record_attendance(name):
    import datetime
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    attendance_records.append({"name": name, "timestamp": timestamp})

def auto_mail():
    sender_email = "lordwinsam21@gmail.com"
    receiver_email = "recipient@gmail.com"
    password = "your_password"  # Use your actual email password or app-specific password
    smtp_server = "smtp.gmail.com"  # Gmail SMTP server
    smtp_port = 465  # SSL port for Gmail

    message = MIMEMultipart("alternative")
    message["Subject"] = "Test Email"
    message["From"] = sender_email
    message["To"] = receiver_email

    text = "This is a test email."
    part = MIMEText(text, "plain")
    message.attach(part)

    try:
        with smtplib.SMTP_SSL(smtp_server, smtp_port) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message.as_string())
        print("Test email sent successfully to", receiver_email)
    except Exception as e:
        print("Error sending test email:", str(e))

if __name__ == "__main__":
    print("Starting the QR code scanner. Press 'q' to quit.")
    mainMenu()

    # After scanning completes, print all attendance records
    print("\nAttendance Records:")
    for record in attendance_records:
        print(f"Name: {record['name']}, Time: {record['timestamp']}")
