import boto3



client = boto3.client('s3')

bucket_name = "manish19950704"

client.delete_bucket(Bucket=bucket_name)

print("S3 Bucket has been deleted")



#Delete bucket with aws resource

# resource = boto3.resource('s3')

# bucket_name = "manish19950704"

# s3_bucket =resource.Bucket(bucket_name)

# s3_bucket.delete()

# print(" This {} bucket has been deleted  ".format(s3_bucket))
