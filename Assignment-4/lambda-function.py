import boto3
import json
from datetime import datetime

specific_volume_id = 'vol-05b137467c1f06601'
ec2 = boto3.client('ec2', region_name='ap-northeast-2')

def lambda_handler(event, context):
    res = ec2.create_snapshot(
        Description="This is a backup snapshot of the volume which i have been working on",
        VolumeId=specific_volume_id,
        TagSpecifications=[
            {
                'ResourceType': 'snapshot',
                'Tags': [
                    {
                        'Key': 'Name',
                        'Value': 'Backup-global-Jenkins'
                    },
                ]
            },
        ],
        DryRun=False
    )
    Stuff()
    return json.dumps('Snapshot created successfully')

def Stuff():
    now_naive = datetime.now()
    snapshots = ec2.describe_snapshots(OwnerIds=['self'])
    for snapshot in snapshots['Snapshots']:
        snapshot_time_naive = snapshot['StartTime'].replace(tzinfo=None)
        if (now_naive - snapshot_time_naive).days > 30:
            print(f"Deleting snapshot {snapshot['SnapshotId']}")
            ec2.delete_snapshot(SnapshotId=snapshot['SnapshotId'])

lambda_handler(None, None)
