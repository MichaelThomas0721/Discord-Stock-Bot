import requests
from bs4 import BeautifulSoup
from csv import writer
import subprocess

response = requests.get('URL')

soup = BeautifulSoup(response.text, 'html.parser')

classes = soup.find_all(class_='pq-hdr-bolder') #The html class the stock status is in

for classes in classes:
    string = classes.get_text()
    if " Available In Stores" in classes: #The in stock status message
        subprocess.call(['PATH\\botStart.bat'])  #Enter the path to the botStart.bat
        break
