from django.shortcuts import render
from django.views import View


class Home(View):
    def get(self, request):
        if request.user.is_authenticated:
            return render(request, 'home.html')
        return render(request, 'home-unauth.html')


class CategoriesView(View):
    def get(self, request):
        return render(request,'categories.html')


class SubCategoriesView(View):
    def get(self, request):
        return render(request, 'subCategories.html')


class ProductsView(View):
    def get(self, request):
        return render(request, 'products.html')


class ProductView(View):
    def get(self, request):
        return render(request, 'product.html')
