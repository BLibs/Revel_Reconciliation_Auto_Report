from config import *
from email.message import EmailMessage
import smtplib


# Function used to send the report to the recipient list via email
def send_report_email(file_path, subject):
    msg = EmailMessage()
    msg.set_content(f"Please find attached the '{ABR_EST_NAME} Reconciliation Report' file.")
    msg['Subject'] = subject
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = RECIPIENT_EMAIL

    with open(file_path, 'rb') as file:
        file_content = file.read()
        msg.add_attachment(file_content, maintype='application', subtype='xlsx', filename=f'{ABR_EST_NAME} '
                                                                                          f'Reconciliation Report.xlsx')
    # Send the email
    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
        server.starttls()  # Secure the connection
        server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        server.send_message(msg)
    print("Email sent successfully!")
