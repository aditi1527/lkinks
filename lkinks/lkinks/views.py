from django.http import HttpResponse
from django.template import loader

def homepage(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render({},request))

def imagesave(request):
    import pdb; pdb.set_trace()
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        return render(request, 'core/simple_upload.html', {
            'uploaded_file_url': uploaded_file_url
        })
    return render(request, 'core/simple_upload.html')
    

