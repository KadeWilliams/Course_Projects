from bs4 import BeautifulSoup
import requests

URL = (
    "https://www.payscale.com/college-salary-report/majors-that-pay-you-back/bachelors"
)

response = requests.get(URL).text

soup = BeautifulSoup(response, "html.parser")
data = soup.find_all(class_="data-table__row")


for elem in data:
    elem.find_all(class_="csr-col--school-name")
    elem.find_all(class_="csr-col--school-type")
    print(elem.find(class_="pxl-tooltip  "))
    # elem.find_all(class_="csr-col--school-name")
    # elem.find_all(class_="csr-col--school-name")
    # row_one = elem.find_all(class_="data-table__title")
