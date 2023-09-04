import boto3
client = boto3.client('ec2')
client.start_instances(InstanceIds=['i-00138ef033254ed96'])

client.stop_instances(InstanceIds=['i-00138ef033254ed96'])

client.terminate_instances(InstanceIds=['i-00138ef033254ed96'])


# to understand which instance got terminated :
# we check the request syntax to see what would be the return response:
# https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/terminate_instances.html

resp = client.terminate_instances(InstanceIds=['i-00138ef033254ed96'])
for instance in resp['TerminatingInstances']:
    print(" The instance with id {} Terminated".format(instance['InstanceId']))
