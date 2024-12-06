from boto3 import client
import io
import os
from dotenv import load_dotenv

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
load_dotenv(os.path.join(BASE_DIR, ".env"))

ACCESS_KEY = os.environ.get('AWS_ACCESS_KEY_ID')
SECRET_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')

s3_client = client(
    "s3",
    aws_access_key_id= os.environ.get('AWS_ACCESS_KEY_ID'),
    aws_secret_access_key= os.environ.get('AWS_SECRET_ACCESS_KEY'),
    region_name="ap-northeast-2"
)



def upload_to_s3(file: io.BytesIO, bucket_name: str, file_name: str) -> None:
    s3_client.upload_fileobj(
        file,
        bucket_name,
        file_name,
)

