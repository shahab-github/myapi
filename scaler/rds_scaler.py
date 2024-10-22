import boto3

def scale_down_rds_instances(tag):
    rds = boto3.client('rds')
    instances = rds.describe_db_instances()
    
    for db in instances['DBInstances']:
        if any(t['Value'] == tag for t in db['TagList']):
            rds.modify_db_instance(DBInstanceIdentifier=db['DBInstanceIdentifier'], DBInstanceClass='db.t3.micro')
            print(f"Scaled down RDS instance: {db['DBInstanceIdentifier']}")

def scale_up_rds_instances(tag):
    rds = boto3.client('rds')
    instances = rds.describe_db_instances()
    
    for db in instances['DBInstances']:
        if any(t['Value'] == tag for t in db['TagList']):
            rds.modify_db_instance(DBInstanceIdentifier=db['DBInstanceIdentifier'], DBInstanceClass='db.m5.large')
            print(f"Scaled up RDS instance: {db['DBInstanceIdentifier']}")
