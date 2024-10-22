import boto3

def scale_down_ec2_instances(tag):
    ec2 = boto3.client('ec2')
    instances = ec2.describe_instances(Filters=[{'Name': 'tag:environment', 'Values': [tag]}])
    
    instance_ids = [i['InstanceId'] for r in instances['Reservations'] for i in r['Instances']]
    
    if instance_ids:
        ec2.stop_instances(InstanceIds=instance_ids)
        print(f"Stopped EC2 instances: {instance_ids}")

def scale_up_ec2_instances(tag):
    ec2 = boto3.client('ec2')
    instances = ec2.describe_instances(Filters=[{'Name': 'tag:environment', 'Values': [tag]}])
    
    instance_ids = [i['InstanceId'] for r in instances['Reservations'] for i in r['Instances']]
    
    if instance_ids:
        ec2.start_instances(InstanceIds=instance_ids)
        print(f"Started EC2 instances: {instance_ids}")
