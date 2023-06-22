"""_summary_
Returns:
    _type_: _description_
"""
from datetime import datetime


def get_datetime_from_timestamp(data, key):
    """_summary_

    Args:
        data (_type_): _description_
        key (_type_): _description_

    Returns:
        _type_: _description_
    """
    date_time = data[key]
    if date_time:
        string_time = date_time.replace('/Date(', '').replace(')/', '')
        int_time = int(string_time) / 1000
        date_time = datetime.fromtimestamp(int_time).strftime("%Y-%m-%dT%H:%M:%S.%fz")
    return date_time
    