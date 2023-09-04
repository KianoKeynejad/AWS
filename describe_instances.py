import boto3
client = boto3.client('ec2')

# if we would like to get all the instances without the filter
resp = client.describe_instances()

#or
# apply filters based on instances status:
resp = client.describe_instances(Filters=[{
    'Name': 'instance-state-name',
    'Values': ['running']
}])

# or
# applying filters based on the tag that we gave to our instances
resp = client.describe_instances(Filters=[{
    'Name': 'tag:kian',
    'Values': ['Kourosh']
}])

for reservation in resp['Reservations']:
    for instance in reservation['Instances']:
        print("InstanceId is {}".format(instance['InstanceId']))
        # or
        #print(f"InstanceId is {'InstanceId'}")


