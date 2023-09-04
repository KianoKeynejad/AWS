import boto3
ec2 = boto3.resource('ec2')
sns_client = boto3.client('sns')

backup_filter = [
    {
        'Name': 'tag:kian',
        'Values': ['Kourosh']
    }
]
snapshot_ids = []
# looping through list(ec2.instance)
for instance in ec2.instances.filter(Filters=backup_filter):
    for vol in instance.volumes.all():
        snapshot = vol.create_snapshot(Description='Created by Boto3')
        snapshot_ids.append(snapshot.snapshot_id)

sns_client.publish(
    TopicArn='arn:aws:sns:ap-southeast-2:042656471251:boto3snapshots',
    Subject='EBS Snapshots',
    Message=str(snapshot_ids)
)