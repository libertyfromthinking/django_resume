import json
from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, RedirectView, TemplateView, FormView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .common_mixin import SelfSuperUserRequiredMixin
from django.http import request, HttpResponse, HttpResponseForbidden
from .forms import * 
from django.db.models import Q
from django.views.generic.edit import FormMixin
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import AnonymousUser
# Create your views here.

class BoardLV(ListView):
    model = Board
    paginate_by = 5

# detailview에 댓글 form 추가
class BoardDV(FormMixin,DetailView):
    model = Board
    form_class = CommentForm

    def get_success_url(self):
        return reverse_lazy('board:detail', args=(self.slug,))

    # 댓글의 내용을 입력받았을 때
    def post(self, request, *args, **kwargs):
        form = self.get_form()
        obj = self.get_object()
        owner = request.user

        if form.is_valid() and owner.is_anonymous==False:
            comment = form.save(commit=False)
            comment.board = obj
            comment.author = owner
            comment.save()
            return redirect('board:detail', slug=obj.slug)
        else:
            return redirect('login')
     
    def form_valid(self, form):
        return super().form_valid(form)

class BoardCreateView(LoginRequiredMixin, CreateView):
    model = Board
    form_class = BoardForm
    template_name = 'board/board_image_form.html'
    success_url = reverse_lazy('board:list')
    
    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super(BoardCreateView, self).form_valid(form)

class BoardUpdateView(SelfSuperUserRequiredMixin, UpdateView):
    model = Board
    form_class = BoardForm
    template_name = 'board/board_image_form.html'
    # fields = ['title', 'content', 'image'] # 폼을 수동으로 지정해서 생략
    success_url = reverse_lazy('board:list')

class BoardDeleteView(SelfSuperUserRequiredMixin, DeleteView):
    model = Board
    success_url = reverse_lazy('board:list')

class BoardRedirectView(TemplateView):
    template_name='board/board_access_deny.html'

class SearchFormView(FormView):
    form_class = SearchForm
    template_name = 'board/board_search.html'
    def form_valid(self, form):
        schWord = '%s'%self.request.POST['search_word']
        object_list = Board.objects.filter(Q(title__icontains=schWord)|Q(content__icontains=schWord)).distinct()

        context = {}
        context['form'] = form
        context['search_term'] = schWord
        context['object_list'] = object_list

        return render(self.request, self.template_name, context)

@require_POST
@login_required
def board_like(request):
    slug = request.POST.get('slug', None)
    board = get_object_or_404(Board, slug=slug)
    print(dir(request))
    
    board_like, board_like_created = board.like_set.get_or_create(user=request.user)
    
    if not board_like_created:
        board_like.delete()
        message = "좋아요 취소"
    else:
        message = "좋아요"

    context = {
        'like_count': board.like_count,
        'message': message,
        'nickname': request.user.username,
        }
        
    return HttpResponse(json.dumps(context), content_type='application/json')
                
@login_required
def remove_comment(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    if comment.author==request.user:
        comment.delete()
        board = get_object_or_404(Board, pk=comment.board.id)
        return redirect('board:detail', slug=board.slug)
    else:
        return redirect('board:deny')

    
