# policy from User 
# Author Manish Pandey
# withouth  function

# import boto3

# iam =boto3.client('iam')
# response = iam.detach_user_policy(
#     UserName = "Manish.Pandey",
#     PolicyArn = "arn:aws:iam::aws:policy/AmazonEC2FullAccess"
# )
# print(response)

#WithFunction 

import boto3

def detach_polices(policy_arn, username):
    iam = boto3.client('iam')
    response = iam.detach_user_policy(
        UserName = username,
        PolicyArn = policy_arn
    )
    print(response)
detach_polices('arn:aws:iam::416815474093:policy/PyFullaccess','Manish.Pandey')
