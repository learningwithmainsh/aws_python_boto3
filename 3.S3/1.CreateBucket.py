import boto3



bucket = boto3.resource('s3')

response = bucket.create_bucket(
    Bucket = "manish19950704",
    ACL="private",
    # ACL="public-read-write",
    
    CreateBucketConfiguration= 
    {
        'LocationConstraint': 'ap-south-1'
    }
    



)

print(response)