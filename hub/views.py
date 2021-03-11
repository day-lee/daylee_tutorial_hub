from django.shortcuts import render
from django.http import HttpResponse
from .models import TutorialList, Curriculum
from users import *
from django.views.generic import View, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .filters import TutorialFilter
from django.contrib.auth.models import User


class HomeView(ListView):
	model = TutorialList
	template_name ='index.html'

# class based: html-> object_list
# class TutorialListView(ListView):
#     model = TutorialList
#     template_name = 'tutorial_list.html'
#
# 	def get_context_data(self, **kwargs):
# 		context = super().get_context_data( *kwargs)
# 		context['filter'] = TutorialFilter(self.request.GET, queryset=self.get_queryset())
# 		return context

def TutorialsList(request):
	tutorials = TutorialList.objects.all()
	# tutorial = tutorials.tutoriallist_set.all() parent child relatioship case
	myFilter = TutorialFilter(request.GET, queryset=tutorials)
	tutorials = myFilter.qs #rendered, thrown into filter , filter down, remake var with the filter down data
	return render(request, 'tutorial_list.html', {'tutorials': tutorials, 'myFilter':myFilter})

# <a href="{% url 'tutorial-detail' post.pk %}"></a>
class TutorialDetailsView(DetailView):
    model = TutorialList
    template_name = 'tutorial_detail.html'

class ContactView(ListView):
    model = TutorialList
    template_name = 'contact.html'

def MyCurriculumList(request):

	if request.user.is_authenticated:
		customer = request.user.customer #onetoone rel
		curriculum, created = Curriculum.objects.get_or_create(customer=customer)
		items = curriculum.curriculumitem_set.all()
	else:
		items = []

	context = {'items': items}
#gonna get all the order items that have above curriculum(order) as a parent
#we are able to query child obj by setting the parent value and child object with all lowercase value and underscore and set
	context = {}
	return render(request, 'cart-curriculum_album.html', context)






# def MycurriculumList(request):
# 	tutorials = TutorialList.objects.all()
# 	# tutorial = tutorials.tutoriallist_set.all() parent child relatioship case
# 	myFilter = TutorialFilter(request.GET, queryset=tutorials)
# 	tutorials = myFilter.qs #rendered, thrown into filter , filter down, remake var with the filter down data
# 	return render(request, 'curriculum_list.html', {'tutorials': tutorials, 'myFilter':myFilter})

# class CurriculumGoalEditView(CreateView):
#     model = TutorialList #need to add  goal field to student model
#     template_name = 'curriculum_goal_edit.html'
#     fields = '__all__'







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

