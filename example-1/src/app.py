import boto3

TABLE_NAME="Monitoring"
dynamodb = boto3.client('dynamodb', endpoint_url="http://localhost:4566")


def get_item(country: str):
    try:
        response = dynamodb.get_item(TableName=TABLE_NAME, Key={'Country': country})
    except Exception as e:
        print("Error -> ",e)
    return response['Item']

def update_item(country: str, error_type: str):
    response = dynamodb.update_item(
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
if __name__ == '__main__':

    update_item("ch", "failedReplication")
    update_item("ch", "failedReplication")
    update_item("pl", "failedReplication")
    update_item("ch", "failedReplication")
    update_item("pl", "failedReplication")
    update_item("ch", "failedReplication")
    update_item("ch", "failedRestore")
    update_item("ch", "failedRestore")
    update_item("ch", "failedRestore")
    update_item("pl", "failedRestore")
