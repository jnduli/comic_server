from django.shortcuts import render, reverse, redirect
from concept.models import Concept
from django.contrib import messages

# Create your views here.

def home_page(request, slug=""):
    if (slug == "" ):
        concept = Concept.objects.random()
        if (concept == None):
            return render(request, 'public/homepage.html')
        return redirect(reverse('public:slug', args=[concept.slug]))
    else:
        concept = Concept.objects.get(slug=slug)
        # choose the comic in strip
    context = {
            'concept' : concept
            }
    return render(request, 'public/homepage.html', context)

def next_comic(request, slug):
    current_concept = Concept.objects.get(slug=slug)
    next_comics = Concept.objects.filter(published=True,date_published__gt=current_concept.date_published).order_by('date_published')
    if (next_comics.count() < 1 ):
        messages.info(request,"This is the lates comic. You cannot go later") 
        return redirect(reverse('public:slug', args=[current_concept.slug]))
    else:
        return redirect(reverse('public:slug', args=[next_comics[0].slug]))

def previous_comic(request, slug):
    current_concept = Concept.objects.get(slug=slug)
    prev_comics = Concept.objects.filter(published=True, date_published__lt=current_concept.date_published).order_by('-date_published')
    if (prev_comics.count() < 1 ):
        messages.info(request,"This is the earliest comic. You cannot go earlier")
        return redirect(reverse('public:slug', args=[current_concept.slug]))
    else:
        return redirect(reverse('public:slug', args=[prev_comics[0].slug]))

