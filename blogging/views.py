from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import loader
from blogging.models import Post
from django.shortcuts import render # ?
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView


class BloggingListView(ListView):
    '''
    model = Post
    '''
    #queryset = Post.objects.filter(text__contains = 'are').order_by('-published_date') #filter specific text
    #queryset = Post.objects.exclude(published_date__isnull = 'True').order_by('-published_date') #filter specific text
    queryset = Post.objects.exclude(published_date__exact = None).order_by('-published_date') #filter specific text
    #queryset = Post.objects.order_by('-published_date') # All entries, sorted
    template_name = 'blogging/list.html'


class BloggingDetailView(DetailView):
    model = Post
    template_name = 'blogging/detail.html'


'''
# rewrite our view, same as above but with a shortcut
def list_view(request):
    published = Post.objects.exclude(published_date__exact=None)
    posts = published.order_by('-published_date')
    context = {'posts': posts}
    return render(request, 'blogging/list.html', context)

def detail_view(request, post_id):
    published = Post.objects.exclude(published_date__exact=None)
    try:
        post = published.get(pk=post_id)
    except Post.DoesNotExist:
        raise Http404
    context = {'post': post}
    return render(request, 'blogging/detail.html', context)
'''


''' this is what generic view is doing, more or less
class ListView():
    def as_view(self):
        return self.get
    def get(self, request):
        model_list_name = self.model.__name__.lower() + '_list' # this is why we added poll_list in the .html
        context = {model_list_name:self.model.objects.all()}
        return render(request,self.template_name, context)
class PollListView(ListView):
    model = Poll
    template_name = 'polling/list.html'
'''
