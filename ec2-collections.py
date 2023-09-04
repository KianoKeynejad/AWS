# if you name this file collection it wont work
# collection provides chainability of orders based on the filters to a group of resources

import boto3
ec2 = boto3.resource('ec2')

# all
for instance in ec2.instances.all():
    print(instance)

# filter with region
for instance in ec2.instances.filter(Filters=[
    {
        'Name': 'availability-zone',
        'Values': ['ap-southeast-2']
    }
]):
    print('Instance id is {} and Instance Type is {} '.format(instance.instance_id,instance.instance_type))

# now we can even change the status of one or more instance with resource synthax

ec2.instances.filter(Filters=[
    {
        'Name': 'instance-state-name',
        'Values': ['running']
    }
]).stop()

