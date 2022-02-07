from django.urls import reverse_lazy
from django.views.generic import CreateView

from profileapp.forms import ProfileCreationForm
from profileapp.models import Profile

# Create your views here.

class ProfileCreateView(CreateView):
    model = Profile
    context_object_name = 'target_profile'
    form_class = ProfileCreationForm
    success_url = reverse_lazy('accountapp:hello_world')
    template_name = 'profileapp/create.html'
    
    def form_valid(self, form): # 이미지를 보낼려면 각 계정 정보가 있어야한다. 그러나 지금 만든것은 계정 정보를 안만든다. 이유는 기존 계정을 이용하기 위해서이다.
        temp_profile = form.save(commit=False) # commit=False로 설정하여 DB에 저장하는것이 아닌 임시로 가지고 있는다.
        temp_profile.user = self.request.user # forms에 있는 3가지의 정보는 있지만 user에 대한 정보가 없는 상황, user정보 가져오는 구문이다.
        temp_profile.save()
        
        return super().form_valid(form)