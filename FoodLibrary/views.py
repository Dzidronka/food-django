
# Create your views here.
from django.contrib import messages
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from django.template.defaultfilters import slugify
from django.views.generic import ListView
from taggit.models import Tag
from .models import Product, Comment
from django.utils import timezone
from .forms import ProductForm, CommentForm, LoginForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout


def product_list(request):
    products = Product.objects.filter(created_date__lte=timezone.now()).order_by('-created_date')
    page = request.GET.get('page', 1)
    common_tags = Product.tags.most_common()[:1]
    paginator = Paginator(products, 3)
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)
    return render(request, 'product-list.html', {'products': products, 'common_tags': common_tags})


def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'product-detail.html', {'product': product})


@login_required
def product_add(request):
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.slug = slugify(product.product_name)
            product.author = request.user
            product.save()
            form.save_m2m()
            return redirect('product_detail', pk=product.pk)
    else:
        form = ProductForm()
    return render(request, 'product-add.html', {'form': form})


def tagged(request, slug):
    tag = get_object_or_404(Tag, slug=slug)
    products = Product.objects.filter(tags=tag)
    context = {
        'tag': tag,
        'products': products,
    }
    return render(request, 'product-list.html', context)


@login_required
def product_edit(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == "POST":
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            product = form.save(commit=False)
            product.author = request.user
            product.published_date = timezone.now()
            product.save()
            form.save_m2m()
            return redirect('product_detail', pk=product.pk)
    else:
        form = ProductForm(instance=product)
    return render(request, 'product-edit.html', {'form': form})


@login_required
def product_publish(request, pk):
    product = get_object_or_404(Product, pk=pk)
    product.publish()
    return redirect('product_detail', pk=pk)


@login_required
def product_remove(request, pk):
    product = get_object_or_404(Product, pk=pk)
    product.delete()
    return redirect('product_list')


def about(request):
    return render(request, 'about.html')


def add_comment(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.product = product
            comment.save()
            return redirect('product_detail', pk=product.pk)
    else:
        form = CommentForm()
    return render(request, 'add-comment.html', {'form': form})


@login_required
def comment_approve(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.approve()
    return redirect('product_detail', pk=comment.product.pk)


@login_required
def comment_remove(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.delete()
    return redirect('product_detail', pk=comment.product.pk)


def login_user(request):
    form = LoginForm(request.POST or None)

    context = {
        "form": form
    }

    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")

        user = authenticate(username=username, password=password)

        if user is None:
            messages.info(request, "Wrong username or password. Try again!")
            return render(request, "login.html", context)

        messages.success(request, "Log in successfully!")
        login(request, user)
        return redirect('product_list')
    return render(request, "login.html", context)


def logout_user(request):
    logout(request)
    messages.success(request, "Log out correctly")
    return redirect('product_list')


class SearchResultsView(ListView):
    model = Product
    template_name = 'search-results.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Product.objects.filter(
            Q(product_name__icontains=query) | Q(produced_by__icontains=query)
            | Q(author__username__icontains=query) | Q(product_type__icontains=query)
        )
        return object_list
