import boto3
import os

def lambda_handler(event, context):
    
    """
    The purpose of this Lambda function is:
    - Retrieve S3 object upload metadata using information contained in the JSON event. More information:
    http://docs.aws.amazon.com/AmazonS3/latest/dev/notification-content-structure.html
    - Push Object name (key), size and object upload time to a DynamoDB table
    Requirements: 
    - DynamoDB table with a FileName primary key
    - Define DynamoDB table in the function environment variables
    - IAM roles with permissions to write DynamoDB
    - Lambda trigger: S3 - ObjectCreated
    """
    
    # Create DynamoDB resource to interact with the AWS API
    resource = boto3.resource('dynamodb')
    
    # Define DynamoDB table using environment variables
    table = resource.Table(os.environ['table_name'])
    
    # Create Variables from S3 Event message
    object_name = event['Records'][0]['s3']['object']['key']
    object_size = event['Records'][0]['s3']['object']['size']
    object_time = event['Records'][0]['eventTime']
    

    print "Adding the following records to the DynamoDB table:"
    print "S3 Object Name: %s" % object_name
    print "S3 Object Size in bytes: %s" % object_size
    print "S3 Object Upload time, based on when S3 processed the request: %s" % object_time
 
    # Push metadata to DynamoDB table 
    print "Pushing values to DynamoDB table %s" % os.environ['table_name']
    table.put_item(Item={'FileName':object_name,'FileSize':object_size, 'TimeStamp':object_time})
