from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect, HttpResponseBadRequest, Http404
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from rest_framework import status


class SelfSuperUserRequiredMixin(LoginRequiredMixin):
    """
    로그인 유저가 아니면 로그인 페이지로
    슈퍼유저 이거나 본인이면 진행
    """

    def dispatch(self, request, *args, **kwargs):
        try:
            instance = get_object_or_404(self.model, slug=kwargs.get('slug', ''))
            login_check_mixin = super().dispatch(request, *args, **kwargs)
            if login_check_mixin.status_code == status.HTTP_200_OK:
                if request.user.is_superuser:   # admin계정이면 모든 권한 가짐
                    pass
                elif instance.owner.username != request.user.username:  # board 객체 owner와 다르면 권한거부 페이지
                    return HttpResponseRedirect(reverse_lazy('board:deny'))
            return login_check_mixin
        except Http404:
            return HttpResponseBadRequest()
