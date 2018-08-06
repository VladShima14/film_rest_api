import requests
import json
import time

from django.shortcuts import render


def index(request):

    context = {}

    if request.method == 'POST':
        start_time_main = time.time()
        r_index = requests.get("http://127.0.0.1:8000/api/v1/")
        r_films = requests.get("http://127.0.0.1:8000/api/v1/film/")
        r_genres = requests.get("http://127.0.0.1:8000/api/v1/genre/")
        api_request_time = time.time() - start_time_main

        if r_index.status_code == 200 and r_films.status_code == 200 \
                and r_genres.status_code == 200:

            _result = "Successfully connected to local API!"
            index_result = json.loads(r_index.content.decode('utf-8'))
            films_result = json.loads(r_films.content.decode('utf-8'))
            genres_result = json.loads(r_genres.content.decode('utf-8'))

            context = {
                'index_result': index_result,
                'films_result': films_result,
                'genres_result': genres_result,
            }
        else:
            _result = "Something went wrong with connection to local API"

        context.update({
            "connection_result": _result,
            'api_request_time': api_request_time,
        })

    return render(request, 'get_api/index.html', context)
