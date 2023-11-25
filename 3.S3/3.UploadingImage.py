# import boto3


# client = boto3.client('s3')


# with open('manish.png', 'rb') as f:
#     data = f.read()


# response = client.put_object(
#     ACL="public-read-write",
#     Bucket = "learningwithmanish",
#     Body=data,
#     Key='manish.png'

# )

# print(response)

import boto3
from botocore.exceptions import ClientError

# Create an S3 client
client = boto3.client('s3')

# Specify your bucket name and file name
bucket_name = "learningwithmanish"
file_name = "manish.png"

try:
    # Open the file and read its contents
    with open(file_name, 'rb') as f:
        data = f.read()

    # Upload the file to S3
    response = client.put_object(
        ACL="public-read",  # Change ACL if needed
        Bucket=bucket_name,
        Body=data,
        Key=file_name
    )

    # Print the response
    print(response)

except ClientError as e:
    # Handle exceptions and print error messages
    print(f"Error uploading file to S3: {e}")


