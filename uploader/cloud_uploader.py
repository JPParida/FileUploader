"""Google Cloude Storage Uploader"""

import os # Importing the os module for file path operations
from google.cloud import storage # Google Cloude Storage client library


class GoogleCloudeStorageUploader:
    """
    Class for uploading files to Google Cloud Storage
    
    Attributes:
    bucket_name (str): The Name of the Google Cloud Storage bucket.
    client (storage.Client): The Google Cloud Storage client object
    bucket (storage.Bucket): The Google Cloud Storage bucket object
    """

    def __init__(self, bucket_name: str):
        """
        Initializes GCSUploader with the given GCS bucket name.
        
        Args:
        bucket_name (str): The Name of the GCS bucket.
        """
        self.client = storage.Client() # creating a Google Cloud Storage Client
        self.bucket = self.client.bucket(bucket_name) # getting the bucket object

    def upload_file(self, file_path):
        """
        Uploads a file to the Google Cloud Storage bucket.
        
        Args:
            file_path (str): The path to the file to be uploaded.
        """
        try:
            blob = self.bucket.blob(os.path.basename(file_path)) #creating the blob object for the file
            blob.upload_from_filename(file_path)  # uploading the file to the Google Cloud Storage bucket
            print(f"Upload Successful: {file_path}") 
        except FileNotFoundError:
            print(f"File not found: {file_path}")
        except Exception as e:
                print(f"An error occurred: {str(e)}")