import json
import logging
from decimal import Decimal

from common.exceptions import CustomExceptions

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def build_response(status_code, body=None):
    """
    Args:
        status_code (str): _description_
        body (_type_, optional): _description_. Defaults to None.

    Returns:
        _type_: _description_
    """
    try:
        response = {
            'statusCode': status_code,
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
            }
        }
        if body is not None:
            response['body'] = json.dumps(body, default=decimal_to_float)
        return response
    except CustomExceptions as err:
        return logger.exception('%s', err)


def decimal_to_float(obj):
    """
    Args:
        obj (json): _description_

    Returns:
        _type_: _description_
    """
    if isinstance(obj, Decimal):
        return str(obj)
    return obj
