import os
from minio import Minio

'''
    1. Install MinIO Python SDK
    pip3.9 install minio

    2. Export Environment Variables
    source export_env.sh

    3. MinIO Python SDK API
    https://docs.min.io/docs/python-client-api-reference.html
'''

def get_s3_server():
    minioClient = Minio(os.environ['S3_ENDPOINT_URL'],
                        access_key=os.environ['AWS_ACCESS_KEY_ID'],
                        secret_key=os.environ["AWS_SECRET_ACCESS_KEY"],
                        secure=False)
    return minioClient


def download_artifacts():

    print("initializing connection to s3 server...")
    minioClient = get_s3_server()
    data_file = minioClient.fget_object("mlflow", "data.csv", "download/data.csv")
    print("download successful")

download_artifacts()

