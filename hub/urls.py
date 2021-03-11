from django.urls import path
from . import views
from .views import  HomeView, TutorialDetailsView, ContactView #, EditGoalView #,TutorialListView,

urlpatterns = [
	# path('', views.index, name='index'),
	# path('', TutorialListView.as_view, name='index'),
	path('', HomeView.as_view(), name='index'),
	path('tutorial_list/', views.TutorialsList, name='tutorial_list'), #TutorialListView.as_view()
	path('tutorial_details/<int:pk>', TutorialDetailsView.as_view(), name='tutorial_detail'),
	path('contact/', ContactView.as_view(), name='contact'),
	# path('register/', ResistrationView.as_view(), name='registration'),
	# path('login/', LoginView.as_view(), name='login'),

	path('curriculum_list/', views.MycurriculumList, name='curriculum_list'),
	# path('my_goal/<int:pk>', CurriculumGoalEditView.as_view(), name="curriculum_goal_edit"),

]