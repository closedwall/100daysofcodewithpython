import os
import smtplib
from datetime import datetime
from email.mime.text import MIMEText
from random import randint

import pandas as pd
from dotenv import load_dotenv

load_dotenv()
my_email = os.getenv('MY_EMAIL')
my_password = os.getenv('APP_PASSWORD')


def prepare_birthday_message(subject, to_email, from_email, name):
    file_name = f"letter_templates/letter_{randint(1, 3)}.txt"
    with open(file_name, 'r', encoding="utf-8") as f:
        letter_content = f.read()
        letter_content = letter_content.replace("[NAME]", name)
    msg = MIMEText(letter_content, 'plain')
    msg['Subject'] = subject
    msg['From'] = from_email
    msg['To'] = to_email
    return msg


def send_mail(email, password, message):
    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as connection:
            connection.starttls()
            connection.login(email, password)
            connection.send_message(message)
    except smtplib.SMTPException as e:
        print(e)
    else:
        print('Email sent successfully')

# ---------------------------------- program starts here -------------------------------------


subject = "Happy Birthday!"
df = pd.read_csv('birthdays.csv')
candidates = df.to_dict(orient="records")
now = datetime.now()
current_month = now.month
current_date = now.day
for candidate in candidates:
    if current_month == candidate['month'] and current_date == candidate['day'] or 1:
        wishing = prepare_birthday_message(subject, candidate["email"], my_email, candidate["name"])
        send_mail(my_email, my_password, wishing)
    else:
        print("Nobody's birthday today")



