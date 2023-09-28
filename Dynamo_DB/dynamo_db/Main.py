import json
import logging

from common.custom_encoder import build_response
from dynamo_db.utils import get_product, get_products, modify_product, save_product, delete_product

logger = logging.getLogger()
logger.setLevel(logging.INFO)

GET_METHOD = 'GET'
POST_METHOD = 'POST'
PATCH_METHOD = 'PATCH'
DELETE_METHOD = 'DELETE'
HEALTH_PATH = '/health'
PRODUCT_PATH = '/product'
PRODUCTS_PATH = '/products'


def lambda_handler(event, context):
    """
    Args:
        event (json): _description_
        context (object): _description_
    """
    logger.info(context)
    http_method = event['httpMethod']
    path = event['path']
    if http_method == GET_METHOD and path == HEALTH_PATH:
        response_body = {
            "Health": "READY"
        }
        response = build_response(200, response_body)
    elif http_method == GET_METHOD and path == PRODUCT_PATH:
        prod_id = (event['queryStringParameters'])['productId']
        print(prod_id)
        response = get_product(prod_id)
    elif http_method == GET_METHOD and path == PRODUCTS_PATH:
        response = get_products()
    elif http_method == POST_METHOD and path == PRODUCT_PATH:
        request_body = json.loads(event['body'])
        response = save_product(request_body)
    elif http_method == PATCH_METHOD and path == PRODUCT_PATH:
        request_body = json.loads(event['body'])
        response = modify_product(
            request_body['productId'], request_body['updateKey'], request_body['updateValue'])
    elif http_method == DELETE_METHOD and path == PRODUCT_PATH:
        request_body = json.loads(event['body'])
        response = delete_product(request_body['productId'])
    else:
        response = build_response(404, 'Not Found')
    return response
