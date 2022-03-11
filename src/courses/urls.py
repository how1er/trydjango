from django.urls import path
from .views import (
      # my_fbv,
      CourseView,
)


app_name = 'courses'
urlpatterns = [

      # path('', my_fbv , name = 'courses-list'),
      path('', CourseView.as_view(template_name='contact.html'), name = 'courses-list'),

      path('<int:id>/', CourseView.as_view(), name = 'courses-detail'),
     # path('<int:id>/update/', ArticleUpdateView.as_view(), name = 'article-update'),
     # path('<int:id>/delete/', ArticleDeleteView.as_view(), name = 'article-delete'),
     # path('create/', ArticleCreateView.as_view(), name = 'article-create'),

]