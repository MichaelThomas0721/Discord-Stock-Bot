import requests
from bs4 import BeautifulSoup
from csv import writer
import subprocess

response = requests.get('https://www.canadacomputers.com/search/results_details.php?language=en&keywords=rtx+3080')

soup = BeautifulSoup(response.text, 'html.parser')

classes = soup.find_all(class_='pq-hdr-bolder')

for classes in classes:
    string = classes.get_text()
    if " Available In Stores" in classes:
        print("yes")
        subprocess.call(['C:\\Users\\micha\\Documents\\Programming\\CanadaComputerBot\\botStart.bat'])
        break
