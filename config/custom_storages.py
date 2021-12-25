from django.conf import settings
from storages.backends.gcloud import GoogleCloudStorage
from storages.utils import setting
from urllib.parse import urljoin


class StaticStorage(GoogleCloudStorage):

    bucket_name = setting('GS_BUCKET_NAME')
    location = "static/"

class UploadStorage(GoogleCloudStorage):

    bucket_name = setting('GS_BUCKET_NAME')
    location = "uploads/"
