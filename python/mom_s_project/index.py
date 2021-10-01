from instapy import InstaPy
from os import getenv
from dotenv import load_dotenv

load_dotenv()


user = getenv("USERNAME")
password = getenv("PASSWORD")

session = InstaPy(username=user, password=password)

