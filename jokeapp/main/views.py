from pyjokes import get_joke
from django.shortcuts import render,HttpResponse
from googletrans import Translator
import asyncio
# Create your views here.
translator = Translator()
async def home(request):
    joke_en=get_joke(language='en')
    #joke_ar=await translator.translate(joke_en,dest='ar')
    return render(request,'index.html',{'joke':joke_en})

