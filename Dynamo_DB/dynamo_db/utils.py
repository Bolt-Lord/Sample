import logging

import boto3
from custom_encoder import build_response
from exceptions import CustomExceptions

logger = logging.getLogger()
logger.setLevel(logging.INFO)

dynamodb = boto3.resource('dynamodb')
DYNAMO_TABLE_NAME = 'product-inventory'
table = dynamodb.Table(DYNAMO_TABLE_NAME)


def get_products():
    """
    Returns:
        json: Entire values in the Table
    """
    try:
        response = table.scan()
        result = response['Items']
        while 'LastEvaluatedKey' in response:
            response = table.scan(
                ExclusiveStartKey=response['LastEvaluatedKey'])
            result.extend(response['Items'])
        body = {
            "products": response
        }
        return build_response(200, body['products']['Items'])
    except CustomExceptions as err:
        return logger.exception('%s', err)


def get_product(product_id):
    """
    Args:
        product_id (str): _description_

    Returns:
        json: Response from DB
    """
    try:
        prd_id = {"productId": str(product_id)}
        response = table.get_item(Key=prd_id)
        if 'Item' in response:
            return build_response(200, response['Item'])
        return build_response(400, {'Message': f'ProductId: {product_id} not found'})
    except CustomExceptions as err:
        print("FAILED")
        return logger.exception('%s', err)


def save_product(request_body):
    """
    Args:
        request_body (json): from postman
    """
    try:
        table.put_item(Item=request_body)
        body = {
            'Operation': 'SAVE',
            'Message': 'SUCESS',
            'Item': request_body
        }
        return build_response(200, body)
    except CustomExceptions as err:
        return logger.exception('%s', err)


def modify_product(product_id, update_key, update_value):
    """
    Args:
        product_id (str): _description_
        updateKey (str): _description_
        updateValue (_type_): _description_

    Returns:
        response from the DB
    """
    try:
        response = table.update_item(
            Key={'productId': product_id},
            UpdateExpression=f'set {update_key} = :val',
            ExpressionAttributeValues={':val': update_value},
            ReturnValues='UPDATED_NEW'
        )
        body = {
            'Operation': 'UPDATE',
            'Message': 'SUCESS',
            'UpdateAttributes': response
        }
        return build_response(200, body)
    except CustomExceptions as err:
        return logger.exception(' %s', err)


def delete_product(product_id):
    """
    Args:
        product_id (str): primary key

    Returns:
        response from the DB
    """
    try:
        response = table.delete_item(
            Key={
                'productId': product_id
            }
        )
        body = {
            "Operation": "DELETE",
            "Message": "SUCESS",
            "DeleteAttribute": response
        }
        return build_response(200, body)
    except CustomExceptions as err:
        return logger.exception('%s', err)
