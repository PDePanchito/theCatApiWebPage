import requests
from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(['GET'])
def get_data(request):
    # Make a GET request to an external API
    response = requests.get('https://api.thecatapi.com/v1/images/search?limit=10&has_breeds=1&api_key=live_29SBrJGFNPFMKqePAlkIX4XodxU8YjXpDqRDk5Svj5cbcLTQJAdwBcRxWi4IEUJk')

    # Print the response content
    print(response.content)

    # Return a response
    return Response({})
