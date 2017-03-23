from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from pymongo import MongoClient
from bs4 import BeautifulSoup
import requests

# client = MongoClient('mongodb://localhost::27017/')
# db = client.scraper
# collection = db.posts


def find(val):
    search = requests.get("https://en.wikipedia.org/wiki/" + val)
    c = search.content
    soup = BeautifulSoup(c, 'html.parser')
    return soup.prettify()


def index(request):
    return render(request, 'scrape/index.html')


def scraped(request, post_body):
    context = {'body': post_body, 'res': find(post_body)}
    return render(request, 'scrape/results.html', context)


def post(request):
    post_body = request.POST['body']
    return HttpResponseRedirect(reverse('scrape:scraped', args=(post_body,)))
