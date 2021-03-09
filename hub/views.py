from django.shortcuts import render
from django.http import HttpResponse
from .models import TutorialList

from django.views.generic import View, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

class HomeView(ListView):
	model = TutorialList
	template_name ='index.html'


class TutorialListView(ListView):
    model = TutorialList
    template_name = 'tutorial_list.html'

# <a href="{% url 'tutorial-detail' post.pk %}"></a>
class TutorialDetailsView(DetailView):
    model = TutorialList
    template_name = 'tutorial_detail.html'

class ContactView(ListView):
    model = TutorialList
    template_name = 'contact.html'


#----------------------------
# class HomeView(ListView):
#     model = Post
#     template_name = 'dummy-home.html'
#     # ordering = ['-id']
#     ordering = ['-post_date']
#
#     #categories drop down : pass context
#     def get_context_data(self, *args, **kwargs):
#         cat_menu = Category.objects.all()
#         context = super(HomeView, self).get_context_data(*args, **kwargs)
#         context["cat_menu"] = cat_menu
#         return context

# def index(request):
# 	return render(request, 'index.html')

# def tutorials(request):
# 	tutorials = TutorialList.objects.all()
# 	return render(request, 'index.html', {'tutorials': tutorials})