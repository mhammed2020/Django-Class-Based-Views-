from django.shortcuts import render

# Create your views here.

# CBVs  https://ccbv.co.uk/projects/Django/3.0/django.views.generic.list/ListView/
from django.views.generic import ListView,DetailView, CreateView,UpdateView,DeleteView
from . models import Post


#logic with classes

class PostList(ListView) :
    model = Post  
    """context in CBVs in template
in template [object_list ==> context_template, post_list(templteName)]
   we can customize this name with context_object_name = "YOUR CONTEXT"

allow_empty = True 	MultipleObjectMixin
content_type = None 	TemplateResponseMixin
context_object_name = None 	MultipleObjectMixin
extra_context = None 	ContextMixin
http_method_names = ['get', 'post', 'put', 'patch', 'delete', 'head', 'options', 'trace'] 	View
model = None 	MultipleObjectMixin
ordering = None 	MultipleObjectMixin
page_kwarg = 'page' 	MultipleObjectMixin
paginate_by = None 	MultipleObjectMixin
paginate_orphans = 0 	MultipleObjectMixin
paginator_class = <class 'django.core.paginator.Paginator'> 	MultipleObjectMixin
queryset = None 	MultipleObjectMixin
response_class = <class 'django.template.response.TemplateResponse'> 	TemplateResponseMixin
template_engine = None 	TemplateResponseMixin
template_name = None 	TemplateResponseMixin
template_name_suffix = '_list' 	MultipleObjectTemplateResponseMixin

    queryset = None 
     ordering = ['-created_at']

    """
    # template_name = 'post/tem.html'
    # queryset = Post.objects.filter(active=True)
   
    # context_object_name ="posts"

    #other feature
    ordering = ['-created_at']

    def get_queryset(self):
        return Post.objects.filter(active=True)


    
    def get_context_data(self, **kwargs): 
         context = super().get_context_data(**kwargs)

         context['email'] = 'jeddou@gmail.com'

         return context
             
         

   


class PostDetail(DetailView) :
     model = Post

class PostCreate() :
    pass

class PostDelete() :
    pass

class PostUpdate() :
    pass
