"""
Class-based views for handling ad display and user interactions.
"""

from typing import Dict
from datetime import timedelta

from django.utils import timezone
from django.urls import reverse_lazy
from django.db.models import Count, QuerySet
from django.http import HttpResponse, HttpRequest
from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.admin.views.decorators import staff_member_required

from .forms import CommentForm
from .models import Ad, Category, User


class HomeView(ListView):
    """
    Main page view showing recent ads with search functionality.
    """

    model: type[Ad] = Ad
    template_name: str = 'board/home.html'
    context_object_name: str = 'ads'
    paginate_by: int = 10

    def get_queryset(self) -> QuerySet[Ad]:
        """
        Return filtered/sorted queryset based on search and date.
        """

        queryset = self.model.objects.filter(
            created_at__gte=timezone.now() - timedelta(days=30),
            is_active=True
        )
        query = self.request.GET.get('q')

        if query:
            queryset = queryset.filter(title__icontains=query)

        return queryset

    def get_context_data(self, **kwargs) -> Dict[str, object]:
        """
        Add categories to template context.
        """

        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()

        return context


class CategoryAdsView(ListView):
    """
    Category-specific ad listing with filtering/sorting.
    """

    model: type[Ad] = Ad
    template_name: str = 'board/category_ads.html'
    context_object_name: str = 'ads'
    paginate_by: int = 10

    def get_queryset(self) -> QuerySet[Ad]:
        """
        Return filtered/sorted ads for specific category.
        """

        category = get_object_or_404(Category, id=self.kwargs['pk'])
        queryset = category.ads.filter(is_active=True)

        # Price filtering
        if min_price := self.request.GET.get('min_price'):
            queryset = queryset.filter(price__gte=min_price)

        if max_price := self.request.GET.get('max_price'):
            queryset = queryset.filter(price__lte=max_price)

        # Date filtering
        if date_filter := self.request.GET.get('date_filter'):
            days = 7 if date_filter == 'week' else 30
            queryset = queryset.filter(created_at__gte=timezone.now() - timedelta(days=days))

        # Sorting
        sort_by = self.request.GET.get('sort_by', '-created_at')

        return queryset.order_by(sort_by)

    def get_context_data(self, **kwargs) -> Dict[str, object]:
        """
        Add category and categories to template context.
        """

        context = super().get_context_data(**kwargs)
        context['category'] = get_object_or_404(Category, id=self.kwargs['pk'])
        context['categories'] = Category.objects.all()

        return context


class UserAdsView(ListView):
    """
    User-specific ad listing view.
    """

    model: type[Ad] = Ad
    template_name: str = 'board/user_ads.html'
    context_object_name: str = 'user_ads'
    paginate_by: int = 10

    def get_queryset(self) -> QuerySet[Ad]:
        """
        Return active ads for specific user.
        """

        user = get_object_or_404(User, id=self.kwargs['user_id'])

        return user.ads.filter(is_active=True)

    def get_context_data(self, **kwargs) -> Dict[str, object]:
        """
        Add user and categories to template context.
        """

        context = super().get_context_data(**kwargs)
        context['user'] = get_object_or_404(User, id=self.kwargs['user_id'])
        context['categories'] = Category.objects.all()

        return context


class AdDetailView(DetailView, CreateView):
    """
    Detailed view for individual ads.
    """

    model: type[Ad] = Ad
    template_name: str = 'board/ad_detail.html'
    context_object_name: str = 'ad'
    form_class = CommentForm
    success_url = reverse_lazy('ad_detail')

    def get_success_url(self) -> str:
        """
        Redirect to the same ad detail page after comment submission.
        """

        return reverse_lazy('ad_detail', kwargs={'pk': self.object.pk})

    def form_valid(self, form: CommentForm) -> HttpResponse:
        """
        Associate comment with current user and ad.
        """

        form.instance.user = self.request.user
        form.instance.ad = self.get_object()

        return super().form_valid(form)

    def get_context_data(self, **kwargs) -> Dict[str, object]:
        """
        Add comment count and categories to template context.
        """

        context = super().get_context_data(**kwargs)
        context['comment_form'] = self.get_form()
        context['comments_count'] = self.object.comments.count()
        context['categories'] = Category.objects.all()

        return context


@staff_member_required
def statistics_view(request: HttpRequest) -> HttpResponse:
    """
    Admin-only statistics view.
    """

    context = {
        'total_ads': Ad.objects.count(),
        'active_ads': Ad.objects.filter(is_active=True).count(),
        'inactive_ads': Ad.objects.filter(is_active=False).count(),
        'categories': Category.objects.annotate(ads_count=Count('ads')),
        'ads_with_comments': Ad.objects.annotate(comments_count=Count('comments')),
    }

    return render(request, 'board/statistics.html', context)
