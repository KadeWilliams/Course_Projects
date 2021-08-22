import random
import smtplib
import datetime as dt

gmail_email = 'a.python.smtp.test@gmail.com'
gmail_password = 'QJcppZ4y69npg7D'
yahoo_email = 'a.pythonsmtptest@yahoo.com'
yahoo_password = 'strgjdgkrtuuncug'

# date_of_birth = dt.datetime(year=1996, month=7, day=10)
now = dt.datetime.now()
year = now.year
month = now.month
day_of_week = now.weekday()
if day_of_week == 0:
    with open('quotes.txt', 'r') as f:
        quotes = f.readlines()
        random_quote = random.choice(quotes)
    with smtplib.SMTP('smtp.gmail.com') as connection:
        connection.starttls()
        connection.login(user=gmail_email, password=gmail_password)
        connection.sendmail(from_addr=gmail_email, to_addrs=gmail_email,
                            msg=f'Subject:Motivational Monday\n\n{random_quote}')
