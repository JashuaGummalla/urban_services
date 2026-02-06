from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Service, Category

def home(request):
    services = Service.objects.filter(is_active=True)[:6]
    return render(request, 'home.html', {'services': services})

from django.db.models import Q

class ServiceListView(ListView):
    model = Service
    template_name = 'services/service_list.html'
    context_object_name = 'services'

    def get_queryset(self):
        queryset = super().get_queryset()
        category_slug = self.request.GET.get('category')
        query = self.request.GET.get('q')
        
        if category_slug:
            queryset = queryset.filter(category__slug=category_slug)
        
        if query:
            queryset = queryset.filter(
                Q(name__icontains=query) | 
                Q(description__icontains=query) |
                Q(category__name__icontains=query)
            )
            
        return queryset.filter(is_active=True)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        if self.request.GET.get('q'):
            context['search_query'] = self.request.GET.get('q')
        return context

class ServiceDetailView(DetailView):
    model = Service
    template_name = 'services/service_detail.html'
    context_object_name = 'service'
