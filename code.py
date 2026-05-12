import json
import boto3
import uuid
from datetime import datetime

# Initialize S3 client
s3 = boto3.client('s3')

def lambda_handler(event, context):
    # This loop processes messages from SQS
    for record in event['Records']:
        # 1. Get the message body (the event data)
        event_data = record['body']
        
        # 2. Create a unique filename with a timestamp
        timestamp = datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
        file_name = f"event-log-{timestamp}-{uuid.uuid4()}.json"
        
        # 3. Define the bucket name (matching your image_f16f37.png)
        bucket_name = 'u103-s3'
        
        # 4. Upload the JSON file to S3
        try:
            s3.put_object(
                Bucket=bucket_name,
                Key=file_name,
                Body=event_data,
                ContentType='application/json'
            )
            print(f"Successfully stored {file_name} in {bucket_name}")
        except Exception as e:
            print(f"Error: {str(e)}")
            
    return {
        'statusCode': 200,
        'body': json.dumps('Event Log Ingested Successfully')
    }
