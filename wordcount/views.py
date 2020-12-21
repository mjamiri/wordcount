from django.http import HttpResponse
from django.shortcuts import render
import operator


def home(request):
    # return HttpResponse('<h1>Hello<h1/>')
    return render(request, 'home.html')


def about(request):
    # return HttpResponse('<h1>Hello<h1/>')
    return render(request, 'about.html')


def count(request):
    text = request.GET['fulltext']
    # print(text)
    # print(wordlist).

    wordlist = text.split()
    worddict = {}

    for word in wordlist:
        if word in worddict:
            worddict[word] += 1
        else:
            worddict[word] = 1

    sortdict = sorted(worddict.items(), key=lambda item: item[1], reverse=True)
    # sortdict = sorted(worddict.items(),
    #                   key=operator.itemgetter(1), reverse=True)
    # print(sortdict)
    return render(request, 'count.html', {'yourtext': text, 'count': len(wordlist), 'worddict': sortdict})

# def eggs(request):
#     return HttpResponse('<h2>I like egg</h2>')
