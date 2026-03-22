from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Avg
from django.shortcuts import get_object_or_404
from .models import Movie, Comment
from .forms import MovieForm, CommentForm

class MovieListView(ListView):
    model = Movie
    template_name = 'movie_list.html' 
    context_object_name = 'movies'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get('q')
        genre = self.request.GET.get('genre')

        if query:
            queryset = queryset.filter(title__icontains=query)
        if genre:
            queryset = queryset.filter(genre__name=genre)

        return queryset.order_by('-rating')

class MovieDetailView(DetailView):
    model = Movie
    template_name = 'CineBoard/movie_detail.html'  

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = self.object.comments.all()
        context['comment_form'] = CommentForm()
        return context

class MovieCreateView(LoginRequiredMixin, CreateView):
    model = Movie
    form_class = MovieForm
    template_name = 'CineBoard/movie_form.html' 
    success_url = reverse_lazy('cineboard:movie_list')  

class MovieUpdateView(LoginRequiredMixin, UpdateView):
    model = Movie
    form_class = MovieForm
    template_name = 'CineBoard/movie_form.html' 
    success_url = reverse_lazy('cineboard:movie_list') 

class MovieDeleteView(LoginRequiredMixin, DeleteView):
    model = Movie
    template_name = 'CineBoard/movie_confirm_delete.html' 
    success_url = reverse_lazy('cineboard:movie_list')  

class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'CineBoard/comment_form.html'  

    def form_valid(self, form):
        movie = get_object_or_404(Movie, pk=self.kwargs['movie_id'])
        form.instance.author = self.request.user  
        form.instance.movie = movie
        return super().form_valid(form)

    def get_success_url(self):
      
        return reverse_lazy('cineboard:movie_detail', kwargs={'pk': self.kwargs['movie_id']})
