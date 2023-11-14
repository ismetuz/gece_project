from django.shortcuts import render, get_object_or_404
from .models import Category,Products, SliderItem , ContactInfo, MainAdvert


# Create your views here.


def home_view(request):
    product_objects = Products.objects.all()
    category_objects = Category.objects.all()
    slideritem_objects = SliderItem.objects.all()
    contact_objects = ContactInfo.objects.all()
    mainadvert_objects = MainAdvert.objects.all()
    context=dict(
        category_objects = category_objects,
        slideritem_objects = slideritem_objects,
        product_objects = product_objects,
        contact_objects=contact_objects,
        mainadvert_objects = mainadvert_objects,
    )
    return render(request,'page/home_page.html', context)

def category_view(request,category_slug):
    category_objects = Category.objects.all()
    product_objects = Products.objects.all()
    contact_objects = ContactInfo.objects.all()
    category = get_object_or_404(Category, slug=category_slug)
    context = dict(
        category_objects = category_objects,
        category=category,
        slug = category_slug,
        product_objects=product_objects,
        contact_objects=contact_objects,
    )
    return render(request,'page/category_details.html', context)


def all_products(request):
    product_objects = Products.objects.all()
    category_objects = Category.objects.all()
    contact_objects = ContactInfo.objects.all()
    context = dict(
        product_objects=product_objects,
        category_objects=category_objects,
        contact_objects=contact_objects,
    )
    return render(request,'page/all_products.html', context)

def about_us(request):
    product_objects = Products.objects.all()
    category_objects = Category.objects.all()
    slideritem_objects = SliderItem.objects.all()
    contact_objects = ContactInfo.objects.all()
    context=dict(
        category_objects = category_objects,
        slideritem_objects = slideritem_objects,
        product_objects = product_objects,
        contact_objects=contact_objects,
    )
    return render(request,'page/about_us.html', context)

def contact_us(request):
    product_objects = Products.objects.all()
    category_objects = Category.objects.all()
    slideritem_objects = SliderItem.objects.all()
    contact_objects = ContactInfo.objects.all()
    context=dict(
        category_objects = category_objects,
        slideritem_objects = slideritem_objects,
        product_objects = product_objects,
        contact_objects=contact_objects,
    )
    return render(request,'page/contact_us.html', context)