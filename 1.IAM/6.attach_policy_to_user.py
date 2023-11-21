#Attach policy to Users
#Author Manish pandey
import boto3

def attach_polices(policy_arn, username):
    iam = boto3.client('iam')
    response = iam.attach_user_policy(
        UserName = username,
        PolicyArn = policy_arn
    )
    print(response)
attach_polices('arn:aws:iam::416815474093:policy/PyFullaccess','Manish.Pandey')
attach_polices('arn:aws:iam::aws:policy/AmazonEC2FullAccess','Manish.Pandey')