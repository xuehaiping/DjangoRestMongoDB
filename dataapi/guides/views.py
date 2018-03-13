import datetime
from django.http import HttpResponse
from guides.models import Guide, Process


def index(request):
    p1 = Process(text='First Process ever', listOfImage=['url1', 'url2'])
    p2 = Process(text='Second Process ever', listOfImage=['url21', 'url22'])

    g1 = Guide(title='firstGuide',
               authorId='12345',
               listOfProcess=[p1, p2],
               dateTime=datetime.datetime.now(),
               listOfTag=['tag1', 'tag2'],
               listOfCategory=['cat1', 'cat2'])

    g1.save()
    return HttpResponse(str(g1))
