from django.contrib.auth.models import User
from django.http import HttpResponseForbidden


def account_ownership_required(func):
    #페이지에 들어온 유저와 로그인한 유저가 다르면 Forbidden
    def decorated(request, *args, **kwargs):
        user = User.objects.get(pk=kwargs['pk'])
        if not user == request.user:
            return HttpResponseForbidden()
        return func(request, *args, **kwargs)

    return decorated

