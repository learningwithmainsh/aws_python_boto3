import boto3


# def create_access(username):
#     iam = boto3.client('iam')

#     response = iam.create_access_key(
#         UserName=username
#     )

#     print(response)



# create_access('Manish.Pandey')




def update_access():
    iam = boto3.client('iam')
    iam.update_access_key(
        AccessKeyId='AKIAWCDBDMWWSPZGZUGX',
        Status='Inactive',
        UserName='Manish.Pandey'

    )


update_access()




