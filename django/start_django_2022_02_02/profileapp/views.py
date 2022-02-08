from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, UpdateView
from profileapp.decorators import profile_ownership_required

from profileapp.forms import ProfileCreationForm
from profileapp.models import Profile
from django.utils.decorators import method_decorator

# Create your views here.

class ProfileCreateView(CreateView):
    model = Profile
    context_object_name = 'target_profile'
    form_class = ProfileCreationForm
    # success_url = reverse_lazy('accountapp:hello_world') detail에 있는게 더 자연스러워 보이지만, detail의 경우 pk 정보를 추가로 얻어야하기떄문에 그냥 바꾸는 걸로는 안되서 get_success_url 을 오버로딩 해서 사용한다.
    template_name = 'profileapp/create.html'
    
    def form_valid(self, form): # 이미지를 보낼려면 각 계정 정보가 있어야한다. 그러나 지금 만든것은 계정 정보를 안만든다. 이유는 기존 계정을 이용하기 위해서이다.
        temp_profile = form.save(commit=False) # commit=False로 설정하여 DB에 저장하는것이 아닌 임시로 가지고 있는다.
        temp_profile.user = self.request.user # forms에 있는 3가지의 정보는 있지만 user에 대한 정보가 없는 상황, user정보 가져오는 구문이다.
        temp_profile.save()
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse('accountapp:detail', kwargs={'pk': self.object.user.pk})
    
        
@method_decorator(profile_ownership_required, 'get')
@method_decorator(profile_ownership_required, 'post')
class ProfileUpdateView(UpdateView):
    model = Profile
    context_object_name = 'target_profile'
    form_class = ProfileCreationForm
    # success_url = reverse_lazy('accountapp:hello_world')
    template_name = 'profileapp/update.html' 
    
    def get_success_url(self):
        return reverse('accountapp:detail', kwargs={'pk': self.object.user.pk})