from django.http import HttpResponse
from django.shortcuts import render
#pip install wikipedia-api
import wikipediaapi

wiki = wikipediaapi.Wikipedia(user_agent='MyDjangoWikiApp/1.0' ,language='en')
# Create your views here.


def home(request):
    if request.method == 'POST':
        search = request.POST['search']
        try:
            page = wiki.page(search)
            return render(request,'index.html',{'result':page.summary})
        except:
            return HttpResponse("Sorry, I don't know anything about that.")
    return render(request,'index.html')