import boto3
import os
from dotenv import load_dotenv
from botocore.exceptions import NoCredentialsError, ClientError
from src.constants import BUCKET_NAME, DATA_FILE_PATH

load_dotenv()


def upload_file_to_s3(file_path, bucket_name, object_name=None, aws_access_key=None, aws_secret_key=None, region_name="us-east-1"):
    """
    Uploads a file to an S3 bucket.

    :param file_path: Local path to the file
    :param bucket_name: Target S3 bucket name
    :param object_name: S3 object name (defaults to file name)
    :param aws_access_key: AWS Access Key ID
    :param aws_secret_key: AWS Secret Access Key
    :param region_name: AWS region
    :return: True if file was uploaded, else False
    """
    if not os.path.isfile(file_path):
        print(f"Error: File '{file_path}' does not exist.")
        return False

    if object_name is None:
        object_name = os.path.basename(file_path)

    try:
        # Create S3 client
        s3_client = boto3.client(
            's3',
            aws_access_key_id=aws_access_key,
            aws_secret_access_key=aws_secret_key,
            region_name=region_name
        )

        # Upload file
        s3_client.upload_file(file_path, bucket_name, object_name)
        print(f"✅ File '{file_path}' uploaded to '{bucket_name}/{object_name}' successfully.")
        return True

    except FileNotFoundError:
        print("Error: The file was not found.")
    except NoCredentialsError:
        print("Error: AWS credentials not available.")
    except ClientError as e:
        print(f"Error: {e}")
    return False

def read_s3_file(bucket_name, object_key, aws_access_key=None, aws_secret_key=None, region_name="us-east-1"):
    """
    Reads the content of a file from an S3 bucket.

    :param bucket_name: Name of the S3 bucket
    :param object_key: Path/key of the file in the bucket
    :param aws_access_key: AWS Access Key ID (optional if using IAM role or AWS CLI credentials)
    :param aws_secret_key: AWS Secret Access Key (optional)
    :param region_name: AWS region (default: us-east-1)
    :return: File content as string
    """
    try:
        # Create S3 client (uses default credentials if not provided)
        if aws_access_key and aws_secret_key:
            s3_client = boto3.client(
                's3',
                aws_access_key_id=aws_access_key,
                aws_secret_access_key=aws_secret_key,
                region_name=region_name
            )
        else:
            s3_client = boto3.client('s3', region_name=region_name)

        # Get the object from S3
        response = s3_client.get_object(Bucket=bucket_name, Key=object_key)

        # Read and decode file content
        content = response['Body'].read().decode('utf-8')
        return content

    except NoCredentialsError:
        print("Error: AWS credentials not found. Configure them using AWS CLI or pass them explicitly.")
    except ClientError as e:
        print(f"Error accessing S3: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")


if __name__ == "__main__":
    
    AWS_ACCESS_KEY = os.getenv("AWS_ACCESS_KEY")
    AWS_SECRET_KEY = os.getenv("AWS_SECRET_KEY")
    BUCKET_NAME = BUCKET_NAME

    # Upload a file
    upload_file_to_s3(DATA_FILE_PATH, BUCKET_NAME, aws_access_key=AWS_ACCESS_KEY, aws_secret_key=AWS_SECRET_KEY)

