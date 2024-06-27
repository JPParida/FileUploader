"""Setup details."""

from setuptools import setup, find_packages # setuptools for packaging the module

setup(
    name='FileUploader', # Package name
    version='0.1', # Package Version
    description='File upload app', # Package description
    packages=find_packages(), # Autoatcally find packages in the directory
    install_requires=[
        'boto3', # Dependency for AWS S3
        'google_cloud-storage', # Dependency for Google Cloud Storage
        'pytest', # Dependency for pytest
        'pytest-cov' # Dependency for test coverage
    ],
    entry_points={
        'console_scripts':[
            'fileuploader=uploader:main', # Command line script entry point
        ],
    },
)