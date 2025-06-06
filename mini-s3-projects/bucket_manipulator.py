import boto3

from botocore.exceptions import NoCredentialsError

from botocore.exceptions import ClientError

import time

s3 = boto3.client('s3')

def get_account_id():
    account = boto3.client("sts")
    try:
        return account.get_caller_identity()["Account"]
    except NoCredentialsError:
        print('\nSorry, we could not find your account id.')
        while True:    
            account_id = input('Please input new account id: ')
            if len(account_id) == 12:
                print('\nThank you for your cooperation!')
                break
            else:
                print('\nInvalid account id.\nThe aws account id is made up of 12 digits consisting of intergers only.')
                time.sleep(0.3)




def del_bucket(bucket_name, account_id):    
    response = s3.delete_bucket(
        Bucket= bucket_name,
        ExpectedBucketOwner= int(account_id)
    )

def cre_bucket(bucket_name, region_name):
    response = s3.create_bucket(Bucket=bucket_name,  CreateBucketConfiguration={'LocationConstraint': region_name}
    )

def ls_buckets():
    response = s3.list_buckets()
    for bucket in response['Buckets']:
        print(bucket['Name'])

print('\nWelcome to the bucket manipulator!')

time.sleep(0.3)

consent = input("\nThis program takes your aws account id. To consent or not, Enter y/n- ")
while consent != 'y' and consent != 'n':
    time.sleep(0.2)
    consent = input("\nThis program takes your aws account id. To consent or not, Enter y/n- ")
if consent == 'y':
    time.sleep(0.4)
    print('\nThank you for your cooperation.')
    account_id = get_account_id()
    print("\nYour account id is:", account_id)
    time.sleep(0.5)
    print('')
    while True:
        user_options = input("There are currently 4 options to select from for the bucket manipulator.\n\nOption 1: Change account id\nOption 2: List existing s3 buckets\nOption 3: Create s3 bucket\nOption 4: Delete s3 bucket\n\nPlease select 1,2,3,4 or q to quit- ")
        while user_options != '1' and user_options != '2' and user_options != '3' and user_options != '4' and user_options != 'q':
            time.sleep(0.2)
            user_options = input("\nThere are currently 4 options to select from for the bucket manipulator.\nPlease select 1,2,3 or 4 or q to quit- ")
        if user_options == '1':
            print('Welcome to the user id changer.')
            while True:    
                account_id = input('Please input new account id: ')
                if len(account_id) == 12:
                    break
                else:
                    print('\nInvalid account id.\nThe aws account id is made up of 12 digits consisting of intergers only.')
                    time.sleep(0.3)

        elif user_options == '2':
            print('\nWelcome to the bucket lister. Your buckets are:')
            ls_buckets()
        elif user_options == '3':
            print('\nWelcome to the bucket creator.')
            bucket_name = input('What is the name of your new bucket?- ')
            region_name = input('What aws region do you wish your bucket to be in?- ')
            try:
                cre_bucket(bucket_name, region_name)
                print(f'{bucket_name} has been added to your list of s3 buckets!')
            except ClientError as e:
                print(f"❌ Error: {e}")
        elif user_options == '4':
            print('\n Welcome to the bucket deletor.')
            bucket_name = input('What is the name of the bucket you wish to delete?- ')
            try:
                print(f'{bucket_name} has been deleted from your list of s3 buckets!')
                del_bucket(bucket_name, account_id)
            except ClientError as e:
                print(f"❌ Error: {e}")
        elif user_options == 'q':
            print('Thank you for using the bucket manipulator!')
            exit()
else:
    print("This code does not work without your aws account id. Thank you for your time.")
    exit()