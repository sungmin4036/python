from re import template
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.generic import RedirectView, ListView
from django.contrib.auth.decorators import login_required
from articleapp.models import Article

from projectapp.models import Project
from subscribeapp.models import Subscription

# Create your views here.

@method_decorator(login_required, 'get')
class SubscriptionView(RedirectView):
    
    def get_redirect_url(self, *args, **kwargs):
        return reverse('projectapp:detail', kwargs={'pk': self.request.GET.get('project_pk')})
    
    def get(self, request, *args, **kwargs):
        
        project = get_object_or_404(Project, pk=self.request.GET.get('project_pk'))
        # proeject_pk를 가지고있는 Project를 찾는데, 그것이 페이지가 만약 없다면, 되돌아가게 해줌 ==> 예외처리한것
        user = self.request.user
        
        subscription = Subscription.objects.filter(user=user, project=project)
        if subscription.exists():
            subscription.delete()
        else:
            Subscription(user=user, project=project).save()
        # 토글형식으로 구독해놨으면 안해놨으면 상태 저장하는것
        
                
        return super(SubscriptionView, self).get(request, *args, **kwargs)
    
    
@method_decorator(login_required, 'get')
class SubscriptionListView(ListView):
    model = Article
    context_object_name = 'article_list'
    template_name = 'subscripeapp/list.html'
    paginate_by = 5
    
    def get_queryset(self):
        projects = Subscription.objects.filter(user=self.request.user).values_list('project') # 프로젝트에 대해서 리스트화 하는것. ==> models.py 에 있는 user, project 를 리스트화 한다
        article_list = Article.objects.filter(project__in=projects)
        return article_list