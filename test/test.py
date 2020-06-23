import os
import boto3

profile_name = os.environ.get('PROFILE_NAME')
boto3_session = boto3.Session(profile_name=profile_name)

client = boto3_session.client('ec2')
result = client.describe_regions()
regions =  [r['RegionName'] for r in result['Regions']]

print(regions)
