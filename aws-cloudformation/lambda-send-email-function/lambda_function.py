import json

import boto3


def lambda_handler(event, context):
    ses = boto3.client('ses')
    name = event.get('name', '')
    email = event.get('email', '')
    message = event.get('message', '')
    body = f'Name : {name} \n Email : {email} \n Message : {message}'
    ses.send_email(
        Source = 'majesticjay@gmail.com',
        Destination = {'ToAddresses': ['majesticjay@gmail.com']},
        Message = {
            'Subject':{
               'Data':'Message from website',
               'Charset':'UTF-8'
           },
           'Body':{
               'Text':{
                   'Data':body,
                   'Charset':'UTF-8'
               }
           }
        }
    )
    return json.dumps({
        'statusCode': 200,
        'body': 'Email sent successfully.', 
        'Access-Control-Allow-Origin': '*'
    })