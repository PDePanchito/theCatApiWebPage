import requests
from django.http import JsonResponse

def get_cat_images(request):
    response = requests.get('https://api.thecatapi.com/v1/images/search?limit=15&has_breeds=1&api_key=live_29SBrJGFNPFMKqePAlkIX4XodxU8YjXpDqRDk5Svj5cbcLTQJAdwBcRxWi4IEUJk')
    data = response.json()
    urls = [item['url'] for item in data]
    breed_name = [item['breeds'][0]['name'] for item in data]
    description = [item['breeds'][0]['description'] for item in data]
    temperament = [item['breeds'][0]['temperament'] for item in data]
    
    return JsonResponse({'urls': urls, 'breed_name': breed_name, 'cat_description': description, 'cat_temperament': temperament})


