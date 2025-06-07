import boto3
from botocore.exceptions import ClientError

bucket_name = "ranmagennics-init-bucket-003"  # Must be globally unique!

region_name='eu-north-1'

# s3 client for us-east-1 (no config block)
s3 = boto3.client('s3')

try:
    response = s3.create_bucket(Bucket=bucket_name, CreateBucketConfiguration={'LocationConstraint': region_name})
    print(f"✅ Bucket '{bucket_name}' created successfully in {region_name}!")
except ClientError as e:
    print(f"❌ Error: {e}")

