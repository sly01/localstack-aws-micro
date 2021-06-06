import boto3

dynamodb = boto3.resource('dynamodb', endpoint_url="http://localhost:4566")
table = dynamodb.Table('Monitoring')

def get_item(country: str):
    try:
        response = table.get_item(Key={'Country': country})
    except Exception as e:
        print("Error -> ",e)
    return response['Item']

def update_item(country: str, error_type: str):
    response = table.update_item(
        Key={
            'Country': country
        },
        UpdateExpression=f"set {error_type} = {error_type} + :increment",
        ExpressionAttributeValues={
            ':increment': 1
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
