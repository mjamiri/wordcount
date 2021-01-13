from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
import operator


def home(request):
    # return HttpResponse('<h1>Hello<h1/>')
    return render(request, 'home.html')


def about(request):
    # return HttpResponse('<h1>Hello<h1/>')
    return render(request, 'about.html')


class apicount(APIView):
    def post(self, request, format=None):
        text = request.data['text']
        wordlist = text.split()
        sortdict = word_count(wordlist)

        return Response(sortdict)


def count(request):
    text = request.GET['fulltext']
    wordlist = text.split()
    sortdict = word_count(wordlist)
    return render(request, 'count.html', {'yourtext': text, 'count': len(wordlist), 'worddict': sortdict})


def word_count(words):
    worddict = {}

    for word in words:
        if word in worddict:
            worddict[word] += 1
        else:
            worddict[word] = 1

    sort_dic = sorted(worddict.items(), key=lambda item: item[1], reverse=True)

    return sort_dic


# def eggs(request):
#     return HttpResponse('<h2>I like egg</h2>')
