import boto3

BUCKET_NAME = "learningwithmanish"

s3_resource = boto3.resource('s3')

s3_bucket = s3_resource.Bucket(BUCKET_NAME)

print("Listing Filtered File")

for obj in s3_bucket.objects.filter(Prefix="myfile"):
    print(obj.key)