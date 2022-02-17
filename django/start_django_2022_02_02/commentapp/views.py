from django.shortcuts import render
from django.urls import reverse
from django.views.generic import CreateView, DeleteView
from articleapp.models import Article
from commentapp.decorators import comment_ownership_required
from commentapp.form import CommentCreationForm
from commentapp.models import Comment
from django.utils.decorators import method_decorator
# Create your views here.


class CommentCreateView(CreateView):
    model = Comment
    form_class = CommentCreationForm
    template_name = 'commentapp/create.html'
    
    def form_valid(self, form):
        temp_comment = form.save(commit=False)
        temp_comment.article = Article.objects.get(pk=self.request.POST['article_pk'])
        # Article 중에서 objects에서 get을 하는데 pk 가 request에서 받은 POST 중에 article_pk 값을 가지고 있는 Article을 지금 만든 comment 에 temp_comment_article 값을 넣는다
        temp_comment.writer = self.request.user
        temp_comment.save()
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse('articleapp:detail', kwargs={'pk': self.object.article.pk})
    
    
@method_decorator(comment_ownership_required, 'get') 
@method_decorator(comment_ownership_required, 'post') 
class CommentDeleteView(DeleteView):
    model = Comment
    context_object_name = 'target_comment'
    template_name = 'commentapp/delete.html'
    
    def get_success_url(self):
        return reverse('articleapp:detail', kwargs={'pk': self.object.article.pk})