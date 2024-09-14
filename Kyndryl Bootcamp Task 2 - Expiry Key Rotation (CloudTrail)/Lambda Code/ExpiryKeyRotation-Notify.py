import json
import boto3

# Initialize the SES client
ses = boto3.client('ses')

def lambda_handler(event, context):
    # Iterate over the records from DynamoDB stream event
    for record in event['Records']:
        # Check if the event type is 'REMOVE', indicating TTL expiration
        if record['eventName'] == 'REMOVE':
            # Extract the expired item details
            expired_item = record['dynamodb']['Keys']
            item_attributes = record['dynamodb']['OldImage']

            # Extract relevant attributes
            cloudtrail_key = expired_item['cloudtrail_key']['S']
            access_key = item_attributes.get('access_key', {}).get('S', 'N/A')
            created_on = item_attributes.get('created_on', {}).get('S', 'N/A')
            source_ipaddress = item_attributes.get('sourceIPAddress', {}).get('S', 'N/A')
            
            # Create the email content
            subject = "Your IAM Access Key has Expired"
            body_text = (
                f"Hello,\n\nYour IAM access key with the following details has expired:\n\n"
                f"CloudTrail Key: {cloudtrail_key}\n"
                f"Access Key: {access_key}\n"
                f"Created On: {created_on}\n"
                f"Source IP Address: {source_ipaddress}\n\n"
                f"Please renew your key or contact support for more information."
            )
            
            # Define SES email parameters
            response = ses.send_email(
                Source='sender@gmail.com',  # Replace with your verified email address
                Destination={
                    'ToAddresses': ['reciever@gmail.com'],  # Your email address where you want to receive the email
                },
                Message={
                    'Subject': {
                        'Data': subject,
                        'Charset': 'UTF-8'
                    },
                    'Body': {
                        'Text': {
                            'Data': body_text,
                            'Charset': 'UTF-8'
                        }
                    }
                }
            )
            
            # Log the email response
            print(f"Email sent! Message ID: {response['MessageId']}")

    return {
        'statusCode': 200,
        'body': json.dumps('Lambda function executed successfully!')
    }
