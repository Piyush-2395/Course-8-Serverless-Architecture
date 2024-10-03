import boto3
import json

from flask import Flask, request, jsonify, render_template

lambdaFunc = boto3.client('lambda', region_name='ap-northeast-2')
ec2 = boto3.client('ec2', region_name='ap-northeast-2')
iam = boto3.client

app = Flask(__name__)
tags = ['Auto-Stop', 'Auto-Start']

# preset variables 
# instance1 = ''
# instance2 =''

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/subdetails', methods=["POST"])
def subdetails():
    # instance1 = request.form['FirstInsance']
    # instance2 = request.form['SecondInsance']
    # stupid = "Creating instance with tags of {} and {}".format(tags[0], tags[1])
    stupid = "Creating instance with tags of {} and {}".format(tags[0], tags[1])
    createInstances(tags)
    return render_template('index.html',stupid=stupid)


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
    return render_template('index.html',message=jsonify(resp1, resp2))

# Create a new role for Lambda.
# Attach the `AmazonEC2FullAccess` policy to this role. (Note: In a real-world scenario, you would want to limit permissions for better security.)


    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)



   