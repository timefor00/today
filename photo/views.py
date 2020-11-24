from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from .forms import CommentForm
from .models import Photo
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def photo_list(request):
    photos = Photo.objects.all()
    paginator = Paginator(photos, 5)
    page = request.GET.get('page')
    try:
        photos = paginator.page(page)
    except PageNotAnInteger:
        photos = paginator.page(1)
    except EmptyPage:
        photos = paginator.page(paginator.num_pages)
    return render(request, 'photo/photo_list.html', {'photos': photos})


class PhotoUploadView(LoginRequiredMixin, CreateView):
    model = Photo
    fields = ['title', 'photo', 'text']
    template_name = 'photo/photo_upload.html'

    def form_valid(self, form):
        form.instance.author_id = self.request.user.id
        if form.is_valid():
            form.instance.save()
            return redirect('photo:photo_list')
        else:
            return self.render_to_response({'form': form})


class PhotoUpdateView(LoginRequiredMixin, UpdateView):
    model = Photo
    fields = ['title', 'photo', 'text']
    template_name = 'photo/photo_update.html'

    def form_valid(self, form):
        form.instance.author_id = self.request.user.id
        if form.is_valid():
            form.instance.save()
            return redirect('/')
        else:
            return self.render_to_response({'form': form})


def add_comment_to_photo(request, pk):
    photo = get_object_or_404(Photo, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.comment_author = request.user
            comment.photo = photo
            comment.save()
            return redirect('photo:photo_detail', pk=photo.pk)
    else:
        form = CommentForm()
    return render(request, 'photo/add_comment_to_photo.html', {'form': form})