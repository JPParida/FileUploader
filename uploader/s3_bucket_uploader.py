"""Upload files in S3 bucket"""

import os # Importing the os module for file path operations
import boto3 # AWS SDK for Python


class S3BucketUploader:
    """
    Class for uploading files to AWS S3.

    Attributes:
    bucket_name (str): The name of the S3 bucket.
    s3 (boto3.client): The S3 client object.
    """

    def __init__(self, bucket_name: str):
        """
        Initialize the S3Uploader with the given S3 bucket name.

        Args:
        bucket_name (str): The name of the S3 bucket.
        """
        self.s3 = boto3.client('s3')  #Creating an S3 client using boto3
        self.bucket_name = bucket_name #Assigning the name of the S3 bucket

    def upload_file(self, file_path: str):
        """
        Upload a file to the S3 bucket.

        Args:
            file_path (str): The path of the file to upload.
        """
        try:
            # Upload the file to the S3 bucket
            self.s3.upload_file(file_path, self.bucket_name, os.path.basename(file_path))
            print(f"Upload Successful: {file_path}") # Success Message
        except FileNotFoundError:
            print(f"file not found: {file_path}")  # File Not Found Error Message
        except Exception as e:
            print(f"An error occurred: {str(e)}") # Other Error Message