"""Test Google Cloud Storage Uploader"""

import pytest
from unittest.mock import patch
from uploader.cloud_uploader import GoogleCloudeStorageUploader

@patch('uploader.cloud_uploader.storage.Client')
def google_cloud_storage_uploader(mock_storage_client):
    """
    Test case for GoogleCloudStorageUploader.upload_file method

    Args:
        mock_storage_client : Mock object for Google Cloud Storage client
    """
    mock_storage_client().bucket().blob().upload_from_filename.return_value = None

    gcs_uploader = GoogleCloudeStorageUploader('test_bucket')
    gcs_uploader.upload_file('test_file.txt')

    mock_storage_client().bucket().blob().upload_from_filename.assert_called_once_with('test_file.txt')
