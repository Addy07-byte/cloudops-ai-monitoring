import boto3
import datetime

def lambda_handler(event, context):
    cloudwatch = boto3.client('cloudwatch', region_name='us-east-1')

    end_time = datetime.datetime.utcnow()
    start_time = end_time - datetime.timedelta(minutes=10)

    response = cloudwatch.get_metric_statistics(
        Namespace='AWS/EC2',
        MetricName='CPUUtilization',
        Dimensions=[{'Name': 'InstanceId', 'Value': 'i-xxxxxxxxxxxx'}],  # Replace with your Instance ID
        StartTime=start_time,
        EndTime=end_time,
        Period=60,
        Statistics=['Average']
    )

    datapoints = sorted(response['Datapoints'], key=lambda x: x['Timestamp'])
    values = [point['Average'] for point in datapoints]

    print("CPU values:", values)

    if any(v > 80 for v in values):
        print("⚠️ Anomaly detected!")
        return {"anomaly": True}
    else:
        print("✅ All normal")
        return {"anomaly": False"}
