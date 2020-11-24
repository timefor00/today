from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from club.views import *
from cart.cart import Cart
from cart.forms import AddProductForm
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from .forms import *


def studio_home(request):
    return render(request, 'base.html')


def product_in_category(request, category_slug=None):
    cart = Cart(request)
    current_category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available_display=True)

    if category_slug:
        current_category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=current_category)

    return render(request, 'today/list.html', {'current_category': current_category, 'categories': categories, 'products': products, 'cart': cart})


class PhotoListView(ListView):
    model = Review
    template_name = 'today/datail.html'
    context_object_name = 'review'


def product_detail(request, id, product_slug=None):
    product = get_object_or_404(Product, id=id, slug=product_slug)
    add_to_cart = AddProductForm()
    reviews = Review.objects.filter(studio=product)
    return render(request, 'today/detail.html', {'product': product, 'add_to_cart': add_to_cart, 'reviews':reviews})


class ReviewListView(ListView):
    model = Review
    template_name = 'today/datail.html'
    context_object_name = 'review'


class ReviewUploadView(CreateView):
    model = Review
    fields = ['studio','title','photo', 'text']
    template_name = 'today/upload.html'

    def form_valid(self, form):
        form.instance.author_id = self.request.user.id
        if form.is_valid():
            form.instance.save()
            return redirect('/')
        else:
            return self.render_to_response({'form': form})