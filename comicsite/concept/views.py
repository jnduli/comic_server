from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.http import HttpResponse
from django.contrib import messages
from django.shortcuts import redirect
from django.utils import timezone

from .models import Concept
from .forms import ConceptForm
from concept.strip.models import Strip

# Create your views here.

@method_decorator(login_required(login_url=reverse_lazy('auth:login')),name='dispatch')
class ConceptCreate(SuccessMessageMixin, CreateView):
    model = Concept
    form_class = ConceptForm
    # success_url = '/comics/system/' 
    success_message = "Concept successfully created"

    def get_success_url(self):
        return reverse('comics:index')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(ConceptCreate, self).form_valid(form)

@method_decorator(login_required(login_url=reverse_lazy('auth:login')),name='dispatch')
class ConceptList(ListView):
    model = Concept

    def get_queryset(self):
        order = self.request.GET.get('orderby', '-date_created')
        filter_val = self.request.GET.get('filter', '')
        user = self.request.user
        if filter_val == '':
            return Concept.objects.filter(user=user).order_by(order)
        else:
            return Concept.objects.filter(user=user, published = filter_val).order_by(order)

    def get_context_data(self, **kwargs):
        context = super(ConceptList, self).get_context_data(**kwargs)
        context['filter'] = self.request.GET.get('filter', '')
        context['orderby'] = self.request.GET.get('orderby', '-date_created')
        return context
    #  def get_queryset(self):
        #  ordering = self.request.GET.get('ordering', '-date_created')
        #  return Concept.objects.order_by(ordering)
#
    #  def get_ordering(self):
        #  ordering = self.request.GET.get('ordering', '-date_created')
        #  return ordering

@method_decorator(login_required(login_url=reverse_lazy('auth:login')),name='dispatch')
class ConceptDetail(DetailView):
    model = Concept

@method_decorator(login_required(login_url=reverse_lazy('auth:login')),name='dispatch')
class ConceptUpdate(SuccessMessageMixin, UpdateView):
    model = Concept
    # fields = ['title', 'description', 'characters_no', 'conversation', 'deleted']
    form_class = ConceptForm
    success_message = "Concept successfully updated"

    def get_object(self, queryset=None):
        con = Concept.objects.get(id=self.kwargs['pk'])
        return con

    def get_success_url(self):
        return reverse('concept:detail_concept', kwargs={'pk':self.object.id})

def publish_concept(request, concept_id):
    con = Concept.objects.get(id=concept_id)
    try:
        strip = Strip.objects.get(concept=con)
        if (con.published):
            messages.success(request, 'Succesfully unpublished')
            con.published = False
            con.save()
        else:
            messages.success(request, 'Successfully published')
            con.date_published = timezone.now()
            con.published = True
            con.save()
        return redirect(reverse('concept:detail_concept', kwargs={'pk':concept_id}))

    except (Strip.DoesNotExist):
        messages.error(request, 'Failed to publish. Does not have strip')
        return redirect(reverse('concept:detail_concept', kwargs={'pk':concept_id}))
