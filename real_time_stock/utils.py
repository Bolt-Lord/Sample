import json
from datetime import datetime

import requests
from bs4 import BeautifulSoup
from matplotlib import pyplot as plt
from pytz import timezone

FILE_PATH = r'data.json'
START_TIME = datetime.strptime("09:15", "%H:%M")
END_TIME = datetime.strptime("15:30", "%H:%M")


def get_price_and_time(stock):
    current_time = datetime.now(timezone("Asia/Kolkata")).strftime('%H:%M')
    current_datetime = datetime.strptime(current_time, "%H:%M")
    # print(current_datetime)
    if START_TIME <= current_datetime <= END_TIME:
        url = f'https://www.google.com/finance/quote/{stock}:NSE'
        response = requests.get(url, timeout=180)
        soup = BeautifulSoup(response.text, 'html.parser')
        print(soup)
        price = float(soup.find(class_='YMlKec fxKbKc').text.strip(
            '₹').replace(',', ''))

        with open(file=FILE_PATH, mode='r', encoding='utf-8') as data:
            ex_data = json.load(data)
            ex_data['prices'].append(price)
            ex_data['times'].append(current_time)

        with open(file=FILE_PATH, mode='w', encoding='utf-8') as json_file:
            json.dump(ex_data, json_file, indent=4)
        return ex_data
    else:
        print("MARKET CLOSED FILE CLEARED")
        initial_data = {
            'prices': [],
            'times': []
        }
        with open(FILE_PATH, 'w', encoding='utf-8') as new_file:
            json.dump(initial_data, new_file, indent=4)
        return initial_data


def ploting(time, prices, stock):
    plt.plot(time, prices, color='green', linestyle='dashed',
             linewidth=3, marker='o', markerfacecolor='blue', markersize=12)
    plt.xlabel('price')
    plt.ylabel('time')
    plt.title(stock)
    # plt.show()
    plt.savefig('Figure_1.png')
