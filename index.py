import json
import boto3 #pip install boto3  python 3.7

from botocore.exceptions import ClientError

def get_secret():  
    secret_name = "aws_access"
    region_name = "us-east-1"

    # Create a Secrets Manager client
    session = boto3.session.Session()
    client = session.client(
        service_name='secretsmanager',
        region_name=region_name
    )

    get_secret_value_response=""
    try:
        get_secret_value_response = client.get_secret_value(
            SecretId=secret_name
        )
    except ClientError as e:
        raise e

    # Decrypts secret using the associated KMS key.
    secret = get_secret_value_response['SecretString']

    return get_secret_value_response


def lambda_handler(event, context):
    # TODO implement
    Secret-Data=get_secret()['SecretString'];
    print(Secret-Data)
    processed=json.loads(Secret-Data)
    secret_key=processed['secret_key']
    print(secret_key)
    key_id=processed['key_id']
    print(key_id)
# 
Secret-Data=get_secret()['SecretString'];
print(Secret-Data) 
processed=json.loads(akshays)
secret_key=processed['secret_key']
# print(secret_key)
key_id=processed['key_id']
# print(key_id)




#Creating Session With Boto3.
session = boto3.Session(
aws_access_key_id=key_id,
aws_secret_access_key=secret_key
)

#Creating S3 Resource From the Session.
s3 = session.resource('s3')
# update your bucket name 👇
object = s3.Object('<BUCKET_NAME>', 'file_uploaded_by_boto3.txt')

txt_data = b'This is the content of the file uploaded from python boto3'

result = object.put(Body=txt_data)

res = result.get('ResponseMetadata')

if res.get('HTTPStatusCode') == 200:
    print('File Uploaded Successfully')
else:
    print('File Not Uploaded')
