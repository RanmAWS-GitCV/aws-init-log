import boto3
from botocore.exceptions import ClientError

bucket_name = "ranmagennics-init-bucket-001"  # Must be globally unique!

# s3 client for us-east-1 (no config block)
s3 = boto3.client('s3', region_name='us-east-1')

try:
    response = s3.create_bucket(Bucket=bucket_name)
    print(f"✅ Bucket '{bucket_name}' created successfully in us-east-1!")
except ClientError as e:
    print(f"❌ Error: {e}")

