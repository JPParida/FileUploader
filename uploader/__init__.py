""" INIT """

import sys
from .config import Constants
from .file_reader import FileReader
from .s3_bucket_uploader import S3BucketUploader
from .cloud_uploader import GoogleCloudeStorageUploader

def main(root_dir):
    """ 
    Main function to read the files from the directory,
    and upload them to S3 and Google Cloude Storage based on their types.
    """

    file_reader = FileReader(root_dir)
    s3_bucket_uploader = S3BucketUploader(Constants.S3_BUCKET_NAME)
    google_cloud_uploader = GoogleCloudeStorageUploader(Constants.CLOUD_BUCKET_NAME)

    for file in file_reader.get_files():
        #check file extension and upload it to the bucket
        if file.split('.')[-1] in Constants.S3_FILE_TYPE:
            s3_bucket_uploader.upload_file(file)
        elif file.split('.')[-1] in Constants.CLOUD_FILE_TYPE:
            google_cloud_uploader.upload_file(file)


if __name__ == '__main__':
    main(sys.argv[1])  # Running the main function with the directory path argument