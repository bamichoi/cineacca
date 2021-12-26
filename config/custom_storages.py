from django.conf import settings
from storages.backends.gcloud import GoogleCloudStorage
from storages.utils import setting  


class StaticStorage(GoogleCloudStorage):

    bucket_name = setting('GS_BUCKET_NAME')
    location = "static/"
    

class UploadStorage(GoogleCloudStorage):

    bucket_name = setting('GS_BUCKET_NAME')
    location = "uploads/"
    GS_FILE_OVERWRITE = False