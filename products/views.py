from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q, Avg
from django.core.paginator import Paginator
from .models import Product, Category, Brand, Review, Wishlist, ProductImage
from .forms import ReviewForm, ProductFilterForm


def home(request):
    featured_products = Product.objects.filter(featured=True, available=True)[:8]
    new_arrivals = Product.objects.filter(available=True).order_by('-created_at')[:8]
    categories = Category.objects.all()
    brands = Brand.objects.all()
    on_sale = Product.objects.filter(discount_price__isnull=False, available=True)[:6]
    phones = Product.objects.filter(category__slug='smartphones', available=True)[:4]
    watches = Product.objects.filter(category__slug='smartwatches', available=True)[:4]
    return render(request, 'home.html', {
        'featured_products': featured_products,
        'new_arrivals': new_arrivals,
        'categories': categories,
        'brands': brands,
        'on_sale': on_sale,
        'phones': phones,
        'watches': watches,
    })


def product_list(request):
    products = Product.objects.filter(available=True)
    categories = Category.objects.all()
    brands = Brand.objects.all()

    category_slug = request.GET.get('category')
    brand_slug = request.GET.get('brand')
    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')
    sort = request.GET.get('sort', '-created_at')
    query = request.GET.get('q', '')

    if category_slug:
        products = products.filter(category__slug=category_slug)
    if brand_slug:
        products = products.filter(brand__slug=brand_slug)
    if min_price:
        products = products.filter(price__gte=min_price)
    if max_price:
        products = products.filter(price__lte=max_price)
    if query:
        products = products.filter(
            Q(name__icontains=query) |
            Q(description__icontains=query) |
            Q(brand__name__icontains=query) |
            Q(category__name__icontains=query)
        )

    sort_options = {
        'price_asc': 'price',
        'price_desc': '-price',
        'newest': '-created_at',
        'oldest': 'created_at',
        'name_asc': 'name',
    }
    products = products.order_by(sort_options.get(sort, '-created_at'))

    paginator = Paginator(products, 12)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'products/product_list.html', {
        'page_obj': page_obj,
        'products': page_obj,
        'categories': categories,
        'brands': brands,
        'selected_category': category_slug,
        'selected_brand': brand_slug,
        'min_price': min_price,
        'max_price': max_price,
        'sort': sort,
        'query': query,
        'total_count': products.count(),
    })


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, available=True)
    gallery = product.images.all()
    reviews = product.reviews.all()
    related = Product.objects.filter(
        category=product.category, available=True
    ).exclude(id=product.id)[:4]

    user_review = None
    if request.user.is_authenticated:
        user_review = Review.objects.filter(product=product, user=request.user).first()

    in_wishlist = False
    if request.user.is_authenticated:
        wishlist, _ = Wishlist.objects.get_or_create(user=request.user)
        in_wishlist = wishlist.products.filter(id=product.id).exists()

    review_form = ReviewForm()

    rating_dist = {}
    for i in range(1, 6):
        count = reviews.filter(rating=i).count()
        rating_dist[i] = {'count': count, 'pct': int(count / reviews.count() * 100) if reviews.count() > 0 else 0}

    return render(request, 'products/product_detail.html', {
        'product': product,
        'gallery': gallery,
        'reviews': reviews,
        'related': related,
        'user_review': user_review,
        'in_wishlist': in_wishlist,
        'review_form': review_form,
        'rating_dist': rating_dist,
    })


def category_products(request, slug):
    category = get_object_or_404(Category, slug=slug)
    products = Product.objects.filter(category=category, available=True)
    brands = Brand.objects.all()

    sort = request.GET.get('sort', '-created_at')
    sort_options = {
        'price_asc': 'price',
        'price_desc': '-price',
        'newest': '-created_at',
        'name_asc': 'name',
    }
    products = products.order_by(sort_options.get(sort, '-created_at'))

    paginator = Paginator(products, 12)
    page_obj = paginator.get_page(request.GET.get('page'))

    return render(request, 'products/category_products.html', {
        'category': category,
        'page_obj': page_obj,
        'brands': brands,
        'sort': sort,
        'categories': Category.objects.all(),
    })


def search_view(request):
    query = request.GET.get('q', '')
    products = Product.objects.filter(available=True)
    if query:
        products = products.filter(
            Q(name__icontains=query) |
            Q(description__icontains=query) |
            Q(brand__name__icontains=query) |
            Q(category__name__icontains=query)
        )
    paginator = Paginator(products, 12)
    page_obj = paginator.get_page(request.GET.get('page'))
    return render(request, 'products/search_results.html', {
        'page_obj': page_obj,
        'query': query,
        'count': products.count(),
    })


@login_required
def add_review(request, slug):
    product = get_object_or_404(Product, slug=slug)
    if Review.objects.filter(product=product, user=request.user).exists():
        messages.warning(request, 'You have already reviewed this product.')
        return redirect('product_detail', slug=slug)
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.product = product
            review.user = request.user
            review.verified_purchase = True
            review.save()
            messages.success(request, 'Your review has been submitted successfully!')
    return redirect('product_detail', slug=slug)


@login_required
def toggle_wishlist(request, slug):
    product = get_object_or_404(Product, slug=slug)
    wishlist, created = Wishlist.objects.get_or_create(user=request.user)
    if wishlist.products.filter(id=product.id).exists():
        wishlist.products.remove(product)
        messages.info(request, f'"{product.name}" removed from wishlist.')
    else:
        wishlist.products.add(product)
        messages.success(request, f'"{product.name}" added to wishlist!')
    return redirect(request.META.get('HTTP_REFERER', 'wishlist'))


@login_required
def wishlist_view(request):
    wishlist, created = Wishlist.objects.get_or_create(user=request.user)
    return render(request, 'products/wishlist.html', {'wishlist': wishlist})


def info_page(request):
    return render(request, 'pages/info.html')


def contact_page(request):
    if request.method == 'POST':
        name    = request.POST.get('name', '').strip()
        email   = request.POST.get('email', '').strip()
        subject = request.POST.get('subject', '').strip()
        message = request.POST.get('message', '').strip()
        if name and email and subject and message:
            messages.success(request,
                f'Thank you, {name}! Your message has been received. '
                'We will get back to you within 24 hours.')
        else:
            messages.error(request, 'Please fill in all fields.')
    return render(request, 'pages/contact.html')
