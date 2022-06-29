import boto3
ec2 = boto3.resource('ec2')
ec2.Instance('i-0633291d8892c24f9').stop()