from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from django.views.generic import (
    CreateView, DeleteView,  DetailView, ListView, UpdateView
)

from .models import Review
from .forms import ReviewForm

class ReviewCreateView(LoginRequiredMixin, CreateView):
    model = Review
    form_class = ReviewForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class ReviewDeleteView(UserPassesTestMixin, DeleteView):
    model = Review
    success_url = reverse_lazy('reviews:list')

    def test_func(self):
        obj = self.get_object()
        return self.request.user == obj.user


class ReviewDetailView(DetailView):
    model = Review


class ReviewListView(ListView):
    model = Review


class ReviewUpdateView(UserPassesTestMixin, UpdateView):
    model = Review
    form_class = ReviewForm

    def test_func(self):
        obj = self.get_object()
        return self.request.user == obj.user