"""Google Cloude Storage Uploader"""

import os
from google.cloud import storage


class GoogleCloudeStorageUploader:
    """
    Class for uploading files to Google Cloud Storage
    
    Attributes:
    bucket_name (str): The Name of the GCS bucket.
    client (storage.Client): The GCS client object
    bucket (storage.Bucket): The GCS bucket object
    """

    def __init__(self, bucket_name: str):
        """
        Initializes GCSUploader with the given GCS bucket name.
        
        Args:
        bucket_name (str): The Name of the GCS bucket.
        """
        self.client = storage.Client()
        self.bucket = self.client.bucket(bucket_name)

    def upload_file(self, file_path):
        """
        Uploads a file to the Google Cloud Storage bucket.
        
        Args:
            file_path (str): The path to the file to be uploaded.
        """
        try:
            blob = self.bucket.blob(os.path.basename(file_path))
            blob.upload_from_filename(file_path)
            print(f"Upload Successful: {file_path}")
        except FileNotFoundError:
            print(f"File not found: {file_path}")
        except Exception as e:
                print(f"An error occurred: {str(e)}")