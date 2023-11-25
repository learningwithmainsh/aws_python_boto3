import boto3


client = boto3.client('s3')

response = client.create_bucket(
    Bucket = "learningwithmanish",
    ACL = "private",

CreateBucketConfiguration= 
    {
        'LocationConstraint': 'ap-south-1'
    }
)

print(response)