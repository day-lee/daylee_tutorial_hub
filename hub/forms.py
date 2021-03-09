# from django import forms
# from .models import Post
#
# #choice = [('coding', 'coding'), ('sports', 'sports')]
# # choices = Category.objects.all().values_list('name','name') #from model
# # choice_list = []
#
# for item in choices:
#     choice_list.append(item)
#
# class PostForm(forms.ModelForm): #inherit forms. ModelForm allows us to create form fields for our Post model.
#     class Meta:
#         model = Post
#         fields = ('title', 'title_tag', 'author', 'category', 'body')
#
#     #add styling: widget dictionary
#         widgets = {
#             'title': forms.TextInput(attrs={'class': 'form-control'},), #css
#             'title_tag': forms.TextInput(attrs={'class': 'form-control'}),
#             'author': forms.Select(attrs={'class': 'form-control'}), #dropdown
#             'category': forms.Select(choices=choice_list, attrs={'class': 'form-control'}),
#             'body': forms.Textarea(attrs={'class': 'form-control'}),
#         }
#
# class EditForm(forms.ModelForm): #inherit forms. ModelForm allows us to create form fields for our Post model.
#     class Meta:
#         model = Post
#         fields = ('title', 'title_tag', 'body')
#
#     #add styling: widget dictionary
#         widgets = {
#             'title': forms.TextInput(attrs={'class': 'form-control'}), #css
#             #'title_tag': forms.TextInput(attrs={'class': 'form-control'}),
#             #'author': forms.Select(attrs={'class': 'form-control'}), #dropdown
#             'body': forms.Textarea(attrs={'class': 'form-control'}),
#         }
