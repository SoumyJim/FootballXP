from django.http import HttpResponse,JsonResponse
import http.client
import json

# Create your views here.


def index(request):
    connection = http.client.HTTPConnection('api.football-data.org')
    headers = { 'X-Auth-Token': '70b8862862a94dea9b4790c8e71d8a9f' }
    connection.request('GET', '/v2/competitions/PL/matches?status=SCHEDULED', None, headers)
    response = json.loads(connection.getresponse().read().decode())
    print(response)
    return JsonResponse({'resp':response["matches"]})
