import boto3

db = boto3.resource('dynamodb')

table = db.Table('employee')



with table.batch_writer() as batch:
    batch.put_item(
        Item = {
            'emp_id':'5',
            'name':'dhireder',
            'age':'35'
        }
    )

    batch.put_item(
        Item = {
            'emp_id':'6',
            'name':'anand',
            'age':'32'
        }
    )

    batch.put_item(
        Item={
            'emp_id': '7',
            'name': 'sonu',
            'age': '37'
        }
    )