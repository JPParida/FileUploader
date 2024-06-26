"""Upload files in S3 bucket"""

import os
import boto3


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
        self.s3 = boto3.client('s3')
        self.bucket_name = bucket_name

    def upload_file(self, file_path: str):
        """
        Upload a file to the S3 bucket.

        Args:
            file_path (str): The path of the file to upload.
        """
        try:
            self.s3.upload_file(file_path, self.bucket_name, os.path.basename(file_path))
            print(f"Upload Successful: {file_path}")
        except FileNotFoundError:
            print(f"file not found: {file_path}")
        except Exception as e:
            print(f"An error occurred: {str(e)}")