import requests
from bs4 import BeautifulSoup
import smtplib


URL = 'https://www.supersoczewki.com/biomedics-1-day-extra-90-szt'
headers = {
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36'
}


def check_price_supersoczewki(): #sprawdź cenę w supersoczewki
    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.text, features="html.parser")
    product_name = soup.find(class_='name').text.strip() #nazwa produktu
    price = soup.find(id='prCurrent').text.strip() #cena produktu
    conv_price = float(price[:-3].replace(' ', "").replace('zl','').replace(',','.')) #konwersja na floata
    desired_price = 111 #wybrana cena, która nas interesuje by nas powiadomić
    if (conv_price < float(desired_price)):
        send_mail()

def send_mail(): #wyślij maila (konto gmail) na dowolny adres
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login('type gmail account', 'type google device password') #login do servera
    receiver = ('type gmail account') #odbiorca
    subject = 'Your E-Mail Subject' #temat
    body = 'Body Text' + URL
    msg = f"Subject: {subject}\n\n{body}"
    server.sendmail(
        'type gmail account',
        receiver,
        msg.encode("UTF-8")
    )
    server.quit()
check_price_supersoczewki()


