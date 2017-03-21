from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from pymongo import MongoClient

# client = MongoClient('mongodb://localhost::27017/')
# db = client.scraper
# collection = db.posts


def index(request):
    return render(request, 'scrape/index.html')


def view(request, post_body):
    context = {'body': post_body}
    return render(request, 'scrape/results.html', context)


def post(request):
    context = {'body': request.POST['body']}
    return render(request, 'scrape/results.html', context)
