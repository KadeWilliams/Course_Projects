import requests
from datetime import datetime
import smtplib

MY_LAT = 36.153980  # Your latitude
MY_LONG = -95.992775  # Your longitude
USERNAME = 'a.python.smtp.test@gmail.com'
PASSWORD = "QJcppZ4y69npg7D"


def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    # Your position is within +5 or -5 degrees of the ISS position
    if abs(iss_latitude - MY_LAT) <= 5 and abs(iss_longitude - MY_LONG) <= 5:
        return True


def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    time_now = datetime.now().hour
    if time_now <= sunrise or time_now >= sunset:
        return True

# If the ISS is close to my current position

if is_iss_overhead() and is_night():
    with smtplib.SMTP('mail.gmail.com') as connection:
        connection.starttls()
        connection.login(user=USERNAME, password=PASSWORD)
        connection.sendmail(from_addr=USERNAME, to_addrs=USERNAME, msg='Subject:ISS UPDATE\n\nGo outside, the ISS is overhead.')

# BONUS: run the code every 60 seconds.
