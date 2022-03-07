import os
from minio import Minio

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

