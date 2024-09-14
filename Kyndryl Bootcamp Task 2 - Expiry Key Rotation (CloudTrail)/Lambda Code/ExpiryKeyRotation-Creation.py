import json
from datetime import datetime, timedelta
import boto3

#Create a DynamoDB client
table_name='your_dbname'
region_name='your_region'
client_dynamo=boto3.resource('dynamodb',region_name=region_name)
dynamodb=client_dynamo.Table(table_name)

#Function to create an item in DynamoDB table
def put_item_to_dynamodb(item):
    dynamodb.put_item(Item=item)

def lambda_handler(event, context):
    #TODO implement
    print(event)
    data_to_insert={}
    data_to_insert['access_key']=event['detail']['responseElements']['accessKey']['accessKeyId']
    creation_time_str=event['detail']['responseElements']['accessKey']['createDate']
    creation_time = datetime.strptime(creation_time_str, '%b %d, %Y %I:%M:%S %p')
    data_to_insert['created_on'] = creation_time.strftime('%Y-%m-%dT%H:%M:%SZ')
    data_to_insert['sourceIPAddress']=event['detail']['sourceIPAddress']
    data_to_insert['cloudtrail_key']=event['id']

    put_item_to_dynamodb(data_to_insert)
    
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }