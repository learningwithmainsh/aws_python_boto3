
import boto3

s3 = boto3.resource('s3')

copy_source = {
    'Bucket':'learningwithmanish',
    'Key':'Profile.pdf'
}

s3.meta.client.copy(copy_source, 'facecollectionbuckets', 'copied.pdf')