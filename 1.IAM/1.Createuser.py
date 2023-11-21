# create user
#Authother Manish Pandey
import boto3

def create_user(username):
    iam = boto3.client('iam')
    response = iam.create_user(UserName=username)
    print(response)
    
create_user('Manish.Pandey')

# pass username at runtime 

import boto3

def create_user(username):
    iam = boto3.client('iam')
    response = iam.create_user(UserName=username)
    print(response)
    
Input_username =input("Enter Your name to created:")    
create_user(Input_username)