from django.shortcuts import render

# Create your views here.


def upload_select_view(request):

    return render(request, "upload.html")
