import boto3
import json

def lambda_handler(event, context):
    s3 = boto3.client('s3')
    unencrypted_buckets = []

    try:
        response = s3.list_buckets()
        buckets = response['Buckets']

        for bucket in buckets:
            bucket_name = bucket['Name']
            encryption = s3.get_bucket_encryption(Bucket=bucket_name)
            if 'ServerSideEncryptionConfiguration' not in encryption:
                unencrypted_buckets.append(bucket_name)

        if unencrypted_buckets:
            print(f"Unencrypted buckets found: {unencrypted_buckets}")


    except Exception as e:
        print(f"Error checking buckets: {e}")

    return {
        'statusCode': 200,
        'body': json.dumps('Bucket check completed')
    }

lambda_handler(None, None)