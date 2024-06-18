import os
import yagmail

receiver = "reviever@gmail.com"  # receiver email address
body = "Your Ward Failed To Attend The Class"  # email body
filename = "Attendance"+os.sep+"Attendance_2024-06-13_13-06-01.csv"  # attach the file

# mail information
yag = yagmail.SMTP("lordwinsam@gmail.com", "Samofficial@29")

# sent the mail
yag.send(
    to=receiver,
    subject="Attendance Report",  # email subject
    contents=body,  # email body
    attachments=filename,  # file attached
)