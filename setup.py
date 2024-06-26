"""Setup details."""

from setuptools import setup, find_packages

setup(
    name='FileUploader',
    version='0.1',
    description='File upload app',
    packages=find_packages(),
    install_requires=[
        'boto3',
        'google_cloud-storage',
        'pytest',
        'pytest-cov'
    ],
    entry_points={
        'console_scripts':[
            'fileuploader=uploader:main',
        ],
    },
)