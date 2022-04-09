from msilib.schema import ListView
import pytz
from .models import Diary
from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, ListView, DeleteView, UpdateView, DetailView
from .forms import DiaryForm
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect

# Create your views here.
# 認証機能 ユーザーモデルの作成 => allauth => https://rightcode.co.jp/blog/become-engineer/django-diary-app-make-approval-function
# 流れ　＝ models => forms  =>　views => urls => html

class IndexView(TemplateView):

    template_name = 'index.html'


class DiaryCreateView(CreateView):
    
    template_name = 'diary_create.html'
    form_class = DiaryForm
    success_url = reverse_lazy('diary:diary_create_complete')


class DiaryCreateCompleteView(TemplateView):

    template_name = 'diary_create_complete.html'


class DiaryListView(ListView):

    template_name = 'diary_list.html'
    model = Diary


class DiaryDetailView(DetailView):

    template_name = 'diary_detail.html'
    model = Diary


class DiaryUpdateView(UpdateView):

    template_name = 'diary_update.html'
    model = Diary
    fields = ('date', 'title', 'text')
    success_url = reverse_lazy('diary:diary_list')

    def form_valid(self, form):
        # 日記データに対応したフォームオブジェクトを入手（commit=Falseでセーブは行われない）オブジェクトの中に入力したデータが入っている
        diary = form.save(commit=False)
        # フォームの入手後現在時刻を入れる
        # diary.updated_at = pytz.timezone.now()
        # 保存する
        diary.save()
        return super().form_valid(form)


class DiaryDeleteView(DeleteView):

    template_name = 'diary_delete.html'
    model = Diary
    success_url = reverse_lazy('diary:diary_list')

    def delete(self, request, *args, **kwargs):

        self.object = self.get_object()
        success_url = self.get_success_url()
        self.object.delete()
        return HttpResponseRedirect(success_url)
