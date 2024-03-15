from utils import get_price_and_time, ploting

STOCK = 'ITC'


def handler():
    data = get_price_and_time(stock=STOCK)
    ploting(data['times'], data['prices'], STOCK)

handler()
