import boto3
import os
from datetime import datetime

# AWS S3 settings
BUCKET_NAME = 'your-bucket-name'
S3_FOLDER = 'backups/'
LOCAL_DIRECTORY = '/path/to/your/directory/'

def upload_to_s3(file_name, bucket, object_name=None):
    s3 = boto3.client('s3')
    try:
        s3.upload_file(file_name, bucket, object_name or file_name)
        print(f"Successfully uploaded {file_name} to {bucket}")
        return True
    except Exception as e:
        print(f"Failed to upload {file_name} to {bucket}: {e}")
        return False

def backup_directory():
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    backup_file = f"backup_{timestamp}.tar.gz"
    os.system(f"tar -czf {backup_file} -C {LOCAL_DIRECTORY} .")
    
    success = upload_to_s3(backup_file, BUCKET_NAME, S3_FOLDER + backup_file)
    
    if success:
        os.remove(backup_file)
    else:
        print("Backup failed. Check the logs for details.")

if __name__ == "__main__":
    backup_directory()
