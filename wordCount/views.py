from django.http import HttpResponse
from django.shortcuts import render
import operator
def home(request):
    return render(request,'home.html')
def count(request):
    fulltext = request.GET['fulltext']
    #print(fulltext)
    wordlist = fulltext.split()

    wordictionary = {}
    for word in wordlist:
        if word in wordictionary:
            wordictionary[word] += 1
        else:
            wordictionary[word] = 1

    sorteddic = sorted(wordictionary.items(), key=operator.itemgetter(1), reverse=True)
    return render(request,'count.html',{'fulltext':fulltext, 'length' : len(wordlist), 'dic':sorteddic})

def about(request):
    return render(request,'about.html')
