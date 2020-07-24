from django.shortcuts import render


def index(request):
    return render(request, 'downloader/index.html')


def download(request):
    args = {
        'url': request.POST.get('url', '{missing url}')
    }
    return render(request, 'downloader/download.html', args)