from django.shortcuts import render
from django.http import HttpResponseRedirect, FileResponse, JsonResponse

# Create your views here.
def home(request):
    context = {}
    return render(request, 'main/index.html',context)
    
#still look up "serving files with django"
def view_upload(request, folder, filename):

    response = FileResponse( open(f'media/{folder}/{filename}', 'rb') )
    return response