"""Configure Constants"""

class Constants:
    """
    Constants class for defining constants used across the application
    """
    S3_BUCKET_NAME = 's3_bucket_name' # Name of S3 bucket
    S3_FILE_TYPE = ['jpg', 'png', 'svg', 'webp', 'mp3', 'mp4', 'mpeg4', 'wmv', '3gp', 'webm'] # file type for S3 bucket
    CLOUD_BUCKET_NAME = 'cloud_bucket_name' # Name of Google Cloud Storage bucket
    CLOUD_BUCKET_TYPE = ['doc', 'docx', 'csv', 'pdf'] # File type for Cloud Storage