from django.db.models import Count
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import ArticleList, ArticleCategory, ArticleComment


class ArticlesView(ListView):
    template_name = 'article/article_list.html'
    model = ArticleList
    paginate_by = 8
    ordering = ['-create_date']

    def get_queryset(self):
        query = super(ArticlesView, self).get_queryset()
        query = query.filter(is_active=True, is_delete=False)
        category = self.kwargs.get('category')
        if category is not None:
            query = query.filter(categories__url_title__iexact=category)
        return query


class ArticleDetailView(DetailView):
    template_name = 'article/article_details.html'
    model = ArticleList

    def get_queryset(self):
        query = super(ArticleDetailView, self).get_queryset()
        query = query.filter(is_active=True, is_delete=False)
        return query

    def get_context_data(self, **kwargs):
        context = super(ArticleDetailView, self).get_context_data()
        article = kwargs.get('object')
        context['comments'] = ArticleComment.objects.filter(is_delete=False, article_id=article.id,
                                                            parent=None).order_by('-create_date').prefetch_related(
            'articlecomment_set')
        return context


def article_category_component(request):
    s_categories = ArticleCategory.objects.annotate(cat_count=Count('articlecategory')).filter(is_active=True,
                                                                                               is_delete=False)
    context = {
        's_categories': s_categories
    }
    return render(request, 'article/components/article_category_component.html', context)


def send_comment(request: HttpRequest):
    if request.user.is_authenticated:
        article_id = request.GET.get('article_id')
        article_comment = request.GET.get('article_comment')
        parent_id = request.GET.get('parent_id')
        comment = ArticleComment(article_id=article_id, comment_text=article_comment, user_id=request.user.id,
                                 parent_id=parent_id)
        comment.save()
        comments = ArticleComment.objects.order_by('-create_date').filter(article_id=article_id,
                                                                          parent=None).prefetch_related(
            'articlecomment_set')
        context = {
            'comments': comments,
            'comments_count': ArticleComment.objects.filter(article_id=article_id).count()
        }
        return render(request, 'article/components/art_comment-component.html', context)
