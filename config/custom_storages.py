from storages.backends.gcloud import GoogleCloudStorage

class StaticStorage(GoogleCloudStorage):
    location = "static/"
    file_overwrite = False

class UploadStorage(GoogleCloudStorage):
    location = "uploads/"