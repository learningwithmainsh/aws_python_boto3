
import boto3

s3_client = boto3.client('s3')

response = s3_client.get_bucket_policy(Bucket='learningwithmanish')
print(response['Policy'])