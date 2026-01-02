from django.shortcuts import render, redirect
import requests

# Create your views here.
def index(request):
    if request.method == 'POST':
        long_url = request.POST['long_url']
        shortened_url = shorten_url(long_url)
        return render(request,'index.html',{
            'short_url':shortened_url
        })
    return render(request,'index.html')

BITLY_ACCESS_TOKEN = '264bdab62d8249baf7fd80423db9df10b5604e4b'

def shorten_url(long_url):
    url = 'https://api-ssl.bitly.com/v4/shorten'
    headers = {
        'Authorization': f'Bearer {BITLY_ACCESS_TOKEN}',
    }
    data = {'long_url': long_url}
    response=requests.post(url,headers=headers,json=data)

    if response.status_code == 200:
        return response.json()['link']
    else:
        return 'Error shortening url'