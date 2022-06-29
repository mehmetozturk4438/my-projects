import boto3

# Use Amazon S3
s3 = boto3.resource('s3')

# Upload a new file
data = open('s3cb.py', 'rb')
s3.Bucket('mhmt-boto3-bucket').put_object(Key='s3cb.py', Body=data)