from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def GetText(request):
    name = request.GET.get('name', 'Гость')
    message = request.GET.get('message','Привет!' )

    context = {
        'name': name,
        'message': message
    }
    return render(request, 'myapp/get_page.html', context)