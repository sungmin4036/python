from django.contrib.auth.forms import UserCreationForm

class AccountUpdateForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.fields['username'].disabled = True
        # 아이디 변경이 기본으로 가능하게 설정되어있는데, 이것을 없애는것.