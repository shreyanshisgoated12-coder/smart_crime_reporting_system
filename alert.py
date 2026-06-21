import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv
import os

load_dotenv()

EMAIL = os.getenv("EMAIL")
APP_PASSWORD = os.getenv("APP_PASSWORD")
POLICE_EMAIL = os.getenv("POLICE_EMAIL")

def send_alert(crime_type, location, station):
    try:
        
        msg = MIMEMultipart()
        msg['From'] = EMAIL
        msg['To'] = POLICE_EMAIL
        msg['Subject'] = f"🚨 CRIME ALERT: {crime_type}"
        
        body = f"""
        CRIME REPORTED
        
        Crime Type: {crime_type}
        Location: {location}
        Nearest Station: {station['name']}
        Distance: {station['distance']} km
        
        Please respond immediately.
        """
        
        msg.attach(MIMEText(body, 'plain'))
        
        # Send email
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(EMAIL, APP_PASSWORD)
        server.sendmail(EMAIL, POLICE_EMAIL, msg.as_string())
        server.quit()
        
        return True
        
    except Exception as e:
        print(f"Email error: {e}")
        return False