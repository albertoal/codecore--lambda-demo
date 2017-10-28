# S3 Lambda DynamoDB lab

The purpose of this Lambda function is:
    - Retrieve S3 object upload metadata using information contained in the JSON event. More information:
    http://docs.aws.amazon.com/AmazonS3/latest/dev/notification-content-structure.html
    - Push Object name (key), size and object upload time to a DynamoDB table

# Requirements: 
- DynamoDB table with a FileName primary key
- Define DynamoDB table in the function environment variables
- IAM roles with permissions to write DynamoDB
- Lambda trigger: S3 - ObjectCreated
