import boto3

BUCKET_NAME = "learningwithmanish"

s3_resource = boto3.resource('s3')

s3_object = s3_resource.Object(BUCKET_NAME, 'Profile.pdf')

s3_object.download_file('downloaded.pdf')

print("File has been downloaded")