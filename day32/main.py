import smtplib
from email.mime.text import MIMEText

from dotenv import load_dotenv
import os
import datetime as dt
from random import choice

load_dotenv()
my_email = os.getenv('MY_EMAIL')
my_password = os.getenv('APP_PASSWORD')
receiver_email = '20it1047@mitsgwl.ac.in'
email_subject = "Quote of the day"


def prepare_message(subject, to_email, from_email):
    quotes = []
    with open("quotes.txt", 'r', encoding="utf-8") as f:
        for line in f:
            quotes.append(line.strip())

    quote_of_the_day = choice(quotes)
    message, author = quote_of_the_day.split('-')
    body = f"""
    <html>
        <body>
            <h1>Quote of the day</h1>
            <p><i>{message}</i></p>
            <p><b>{author}</b></p>
        </body>
    </html>
    """
    msg = MIMEText(body, 'html')
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


now = dt.datetime.now()
weekday = now.weekday()
if weekday == 6:
    email_message = prepare_message(email_subject, receiver_email, my_email)
    send_mail(my_email, my_password, email_message)
else:
    print("Today is not Monday", weekday)

