import json
import boto3
import paramiko
import sys
import logging
import os
import re
import urllib3

sns_arn = "arn:aws:sns:us-east-1:122350927083:LambdaSFTP"
region_src="eu-east-1"

session = boto3.Session(
)
sns_client = session.client('sns')


def hello(event, context):
    k = paramiko.RSAKey.from_private_key_file("key.pem")
    c = paramiko.SSHClient()
    c.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    print "connecting"
    c.connect( hostname = "35.182.43.77", username = "ubuntu", pkey = k )
    print "connected"
    sftpClient = c.open_sftp()

    response=sftpClient.listdir(path='.')

    text = 'testfile'
    for pattern in response:
        if re.search(pattern, text):
            response = "found a match!"

            return response
        message = "testmessage "

        print("Sending SNS alert")
        sns = boto3.client("sns", region_name=region_src)
        message = "test message david"
        sns_client.publish(TopicArn=sns_arn,Message=message)

        htttp = urllib3.PoolManager()
        data = {"text":"sample message from lambda function"}
        r = htttp.request("POST",
                          "https://hooks.slack.com/services/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",
                          body = json.dumps(data),
                          headers={"Content-Type":"application/json"})
