from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views.generic.base import View
from .models import *

from .forms import ReviewForm,DataForm

def index(request):
    render(request, 'predictions/index.html')

def predictions(request):
    template = loader.get_template("predictions/index.html")
    return HttpResponse(template.render)

class ProductsView(View):

    def get(self,request):
        products = Product.objects.all()
        return render(request,'products/products_list.html',{'products_list':products})

class ProductDetailView(View):

    def get(self,request,slug):
        product = Product.objects.get(url = slug)
        return render(request,'products/product_detail.html',{'product':product})

class AddReview(View):

    def post(self,request,pk):
        form = ReviewForm(request.POST)
        if form.is_valid():
            form = form.save(commit = False)
            form.product_id = pk
            form.save()
        return redirect("/block")
