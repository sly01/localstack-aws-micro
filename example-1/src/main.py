
import os
import boto3
import json


TABLE_NAME="Monitoring"
client = boto3.client('dynamodb', endpoint_url="http://" + os.getenv("LOCALSTACK_HOSTNAME") + ":4566")

def update_item(country: str, error_type: str):
    response = client.update_item(
        TableName=TABLE_NAME,
        Key={
            'Country': {'S': country}
        },
        UpdateExpression=f"set {error_type} = {error_type} + :increment",
        ExpressionAttributeValues={
            ':increment': {'N': '1'}
        },
        ReturnValues='UPDATED_NEW'
    )
    return response

def lambda_handler(event, context):
    print(event)
    data = json.loads(event["body"])
    country = data['country']
    error_type = data['error_type']
    item = update_item(country, error_type)
    response = {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json"
        },
        "body": json.dumps(f"Written item is {item}")
    }
    return response