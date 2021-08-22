import pandas as pd
import datetime as dt
import random
import smtplib

##################### Extra Hard Starting Project ######################

gmail_email = 'a.python.smtp.test@gmail.com'
gmail_password = 'QJcppZ4y69npg7D'
yahoo_email = 'a.pythonsmtptest@yahoo.com'
yahoo_password = 'strgjdgkrtuuncug'

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv
now = dt.datetime.now()
today = (now.month, now.day)

data = pd.read_csv('birthdays.csv')
birthdays_dict = {(v.month, v.day): v for (k, v) in data.iterrows()}

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

if today in birthdays_dict:
    birthday_person = birthdays_dict[today]
    with open(f'letter_templates/letter_{random.randint(1, 3)}.txt', 'r') as f:
        letter = f.read()
        LETTER = letter.replace('[NAME]', birthday_person['name'])

    # 4. Send the letter generated in step 3 to that person's email address.
    with smtplib.SMTP('smtp.gmail.com') as connection:
        connection.starttls()
        connection.login(user=gmail_email, password=gmail_password)
        connection.sendmail(from_addr=gmail_email, to_addrs=birthday_person['email'], msg=f'Subject:Happy Birthday\n\n{LETTER}')



