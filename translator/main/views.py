from django.shortcuts import render
from django.http import HttpResponse
from googletrans import Translator
import asyncio #to prevent the error of never await

# Create your views here.

translator = Translator()
async def home(request):

    if request.method == 'POST':
        text=request.POST['translate']
        language=request.POST['language']
        translation= await translator.translate(text,dest=language)
        return render(request,'index.html',{'translated':translation.text})
    return render(request,'index.html')