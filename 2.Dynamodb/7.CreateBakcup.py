#creating backup
# import boto3

# db = boto3.client('dynamodb')



# response = db.create_backup(
#     TableName='employee',
#     BackupName='employeeBackUp'
# )

# print(response)


#delete   backup

import boto3

db = boto3.client('dynamodb')




response = db.delete_backup(
    BackupArn='arn:aws:dynamodb:ap-south-1:416815474093:table/employee/backup/01700156157011-27c13742'

)

print(response)