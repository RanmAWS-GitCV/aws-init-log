import boto3

s3 = boto3.client('s3')

def get_account_id():
    client = boto3.client("sts")
    return client.get_caller_identity()["Account"]


print("account id is:", get_account_id())

account_id = get_account_id()

response = s3.delete_bucket(
    Bucket='ranmagennics-init-bucket-001',
    ExpectedBucketOwner= account_id
)
