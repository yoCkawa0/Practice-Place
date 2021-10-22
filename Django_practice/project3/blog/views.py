from django.views import generic

# Create your views here.
class IndexView(TemplateView):
    template_name = "blog/post_list.html"
