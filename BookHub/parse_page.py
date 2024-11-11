import requests
from bs4 import BeautifulSoup

data_user = {"user-agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36 Edg/130.0.0.0"}
url = str(f'http://127.0.0.1:8000/media/books/Prohorenok_N._Python_i_PyQt.Fragment.pdf')
response = requests.get(url , headers = data_user)

print(11)
soup = BeautifulSoup(response.text, "lxml")