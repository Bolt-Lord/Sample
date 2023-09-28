from datetime import datetime

def get_datetime_from_timestamp():
    date_time = '/Date(1691047800000)/'
    string_time = date_time.replace('/Date(', '').replace(')/', '')
    print(string_time)
    int_time = int(string_time) / 1000
    date_time = datetime.fromtimestamp(int_time).strftime("%Y-%m-%dT%H:%M:%S.%fz")
    return date_time


print(get_datetime_from_timestamp())
