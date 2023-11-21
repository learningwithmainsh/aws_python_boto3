#List IAM Policy with Python
#Author Manish Pandey 

import boto3

def list_policies():
    iam = boto3.client('iam')
    paginator = iam.get_paginator('list_policies')
    # for response in paginator.paginate():
    #to view only customer  managed policy use Scope = locla 
    # for response in paginator.paginate(Scope="Local"):
    #for list only AWS managed policy 
    for response in paginator.paginate(Scope="AWS"):
        for policy in response['Policies']:
            policy_name = policy['PolicyName']
            arn = policy['Arn']
            print('Policy Name: {} Arn: {}'.format(policy_name, arn))

list_policies()
