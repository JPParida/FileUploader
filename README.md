# FileUploader
This module reads all the files from the directory and its subdirectories, uploading image and media files to AWS S3 and document files to Google cloud storage.

## Installation

1. Clone the repository:
```bash
git clone https://github.com/JPParida/FileUploader.git
cd FileUploader
```

2. Install the required packages:
```bash
pip install -r requirements.txt
```

### Tests
```bash
pytest --cov=uploader tests/
```

#### Run
```
Run the module by providing the root directory as an argument

python -m uploader <directory_path>
```
