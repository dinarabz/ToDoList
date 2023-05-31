from django.views.generic import ListView, RedirectView

from webapp.forms import ArticleForm
from webapp.models import Article


class IndexView(ListView):
    template_name = 'index.html'
    model = Article
    context_object_name = 'articles'
    ordering = ('created_at',)
    paginate_by = 3
    paginate_orphans = 1


class IndexRedirectView(RedirectView):
    pattern_name = 'index'
