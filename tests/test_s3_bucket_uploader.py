"""Test S3 bucket uploader"""

import pytest
from unittest.mock import patch
from uploader.s3_bucket_uploader import S3BucketUploader

@patch('uploader.s3_bucket_uploader.boto3.client')
def test_upload_file(mock_boto_client):
    """
    Test case for S3BucketUploader.upload_file method.

    Args:
        mock_boto_client : Mock object for boto3 client.
    """

    mock_boto_client().upload_file.return_value = None

    s3_uploader = S3BucketUploader("test_bucket")
    s3_uploader.upload_file("test_file.txt")

    mock_boto_client().upload_file.assert_called_once_with("test_file.txt", "test_bucket", "test_file.txt")