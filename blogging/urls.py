from django.urls import path, include
from blogging.views import BloggingListView
from blogging.views import BloggingDetailView

urlpatterns = [
    path('', BloggingListView.as_view(), name="blog_index"), # When using django generic view, use this format xx.as_view()
    path('posts/<int:pk>/', BloggingDetailView.as_view(), name="blog_detail"),
]

''' Also replace this line in list.html
      {% for post in posts %}
      by   {% for post in post_list %}
'''


''' Also replace this line in detail.html
      <h1>{{ post }}</h1>
      by   <h1>{{ post }}</h1>

      {{ post.text }}
      by {{ object.text }}
'''
