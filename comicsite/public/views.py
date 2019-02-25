from django.shortcuts import render, reverse, redirect
from concept.models import Concept
from django.contrib import messages
from django.conf import settings


def home_page(request, slug=""):
    if slug:
        concept = Concept.objects.get(slug=slug)
        context = {
            'analytics_tracking_id': settings.ANALYTICS_TRACKING_ID,
            'concept': concept
            }
        return render(request, 'public/homepage.html', context)
    else:
        concept = Concept.objects.random()
        if concept is None:
            return render(request, 'public/homepage.html')
        return redirect(reverse('public:slug', args=[concept.slug]))


def next_comic(request, slug):
    current_concept = Concept.objects.get(slug=slug)
    next_comic = Concept.objects\
        .filter(published=True,
                date_published__gt=current_concept.date_published)\
        .order_by('date_published')\
        .first()
    if next_comic:
        return redirect(reverse('public:slug', args=[next_comic.slug]))
    else:
        messages.info(request, "This is the latest comic. You cannot go later")
        return redirect(reverse('public:slug', args=[current_concept.slug]))


def previous_comic(request, slug):
    current_concept = Concept.objects.get(slug=slug)
    prev_comic = Concept.objects\
        .filter(published=True,
                date_published__lt=current_concept.date_published)\
        .order_by('-date_published')\
        .first()
    if prev_comic:
        return redirect(reverse('public:slug', args=[prev_comic.slug]))
    else:
        messages.info(request,
                      'This is the earliest comic. You cannot go earlier')
        return redirect(reverse('public:slug', args=[current_concept.slug]))


def last_comic(request):
    last_comic = Concept.objects.filter(published=True)\
            .order_by('date_published').last()
    return redirect(reverse('public:slug', args=[last_comic.slug]))


def first_comic(request):
    first_comic = Concept.objects.filter(published=True)\
        .order_by('date_published').first()
    return redirect(reverse('public:slug', args=[first_comic.slug]))
