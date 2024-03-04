import requests
from bs4 import BeautifulSoup
from datetime import datetime
from pytz import timezone 
import time
import json

stock = 'ITC'
url = f'https://www.google.com/finance/quote/{stock}:NSE'

prices = None
times = None


def get_price_and_time():
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    price = float(soup.find(class_='YMlKec fxKbKc').text.strip('₹').replace(',', ''))
    current_time = datetime.now(timezone("Asia/Kolkata")).strftime('%I:%M')

    with open(r'real_time_stock/data.json', 'r') as data:
        ex_data = json.load(data)

    ex_data['prices'].append(price)
    ex_data['times'].append(current_time)

    with open(r'real_time_stock/data.json', 'w') as json_file:
        json.dump(ex_data, json_file, indent=4)
