import boto3
from pprint import pprint

db = boto3.resource('dynamodb')

response = db.batch_get_item(
    RequestItems={
        'employee':{
            'Keys':[
                {
                    'emp_id':'1',

                },
                {
                    'emp_id':'5'
                },

                {
                    'emp_id':'6'
                },

                {
                    'emp_id':'4'
                }
            ]
        }
    }
)

pprint(response['Responses'])