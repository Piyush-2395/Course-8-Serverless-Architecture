
import boto3
import json

lambdaFunc = boto3.client('lambda', region_name='ap-northeast-2')
ec2 = boto3.client('ec2', region_name='ap-northeast-2')
iam = boto3.client

tags = ['Auto-Stop', 'Auto-Start']
def createInstances(tags):
    resp1 = ec2.run_instances(
        TagSpecifications=[
            {
                'ResourceType': 'instance',
                'Tags': [
                    {
                        'Key': 'Name',
                        'Value': tags[0]
                    },
                ]
            },
        ],    
        ImageId ='ami-062cf18d655c0b1e8',
        InstanceType='t2.micro',
        MinCount=1,
        MaxCount=1,
        KeyName='Gani_reborne',
    )
    resp2 = ec2.run_instances(
        TagSpecifications=[
            {
                'ResourceType': 'instance',
                'Tags': [
                    {
                        'Key': 'Name',
                        'Value': tags[1]
                    },
                ]
            },
        ],    
        ImageId ='ami-062cf18d655c0b1e8',
        InstanceType='t2.micro',
        MinCount=1,
        MaxCount=1,
        KeyName='Gani_reborne',
    )
    return resp1, resp2

createInstances(tags)