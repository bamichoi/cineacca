from storages.backends.s3boto3 import S3Boto3Storage

class StaticStorages(S3Boto3Storage):
    location = "static/"
    file_overwrite = False

class UploadStorages(S3Boto3Storage):
    location = "uploads/"