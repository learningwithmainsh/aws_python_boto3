# import boto3

# client = boto3.client('s3')



# response = client.delete_object(
#     Bucket = 'learningwithmanish',
#     Key='myfile.txt'
# )

# print(response)



#delete multiple files or objects
import boto3
client = boto3.client('s3')

response = client.delete_objects(
    Bucket = 'facecollectionbuckets',
    Delete = {
        'Objects':[
            {
                'Key':'1.jpg'
            },

            {
                'Key':'2.jpg'
            }


        ]
    }
)

print(response)


