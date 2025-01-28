import subprocess
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from dotenv import load_dotenv
load_dotenv()

def before_all(context):
    pass
    files = os.listdir("./reports")
    for file in files:
        if file in "report.txt":
            continue
        os.remove("./reports/"+file)
    # # os.rmdir("./reports")
    # # if not os.path.exists("./reports"):
    # #     os.mkdir("./reports")
    

def after_all(context):
    print("Suite ended")
    try:
        subprocess.run("allure --version", shell=True)
        # subprocess.run("set path=D:\\Softwares\\allure-2.32.0\\bin", shell=True)
        subprocess.run("allure generate --single-file --clean ./reports", shell=True, check=True)
        print("Allure report generated successfully!")
        
        # Example usage
        send_email_with_attachment(
            "Testing BDD",
            "This is the body of the email.",
            "sawant.prasad0275@gmail.com",
            "./allure-report/index.html"
        )
    except subprocess.CalledProcessError as e:
        print(f"Error generating Allure report: {e}")
       
    
    
def send_email_with_attachment(subject, body, to_email, file_path):
    # Your email details
    from_email = "sawant.prasad0275@gmail.com"
    password = os.getenv('GPWD')

    # Set up the server
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()  # Start TLS (Transport Layer Security)
    server.login(from_email, password)

    # Create the email
    message = MIMEMultipart()
    message['From'] = from_email
    message['To'] = to_email
    message['Subject'] = subject

    # Attach the email body
    message.attach(MIMEText(body, 'plain'))

    # Attach the file
    try:
        with open(file_path, "rb") as attachment:
            # Create the attachment part
            part = MIMEBase('application', 'octet-stream')
            part.set_payload(attachment.read())
            encoders.encode_base64(part)  # Encode the file to base64
            part.add_header('Content-Disposition', f'attachment; filename={file_path.split("/")[-1]}')
            message.attach(part)
    except Exception as e:
        print(f"Could not attach the file: {e}")

    # Send the email
    server.sendmail(from_email, to_email, message.as_string())

    # Close the connection
    server.quit()

