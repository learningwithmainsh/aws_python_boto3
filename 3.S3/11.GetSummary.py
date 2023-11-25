import boto3


s3 = boto3.resource('s3')

object_summary = s3.ObjectSummary("learningwithmanish", "file.pdf")

print(object_summary.bucket_name)
print(object_summary.key)