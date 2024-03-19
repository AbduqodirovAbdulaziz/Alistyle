from django.urls import path
from .views import *

urlpatterns=[
    path('categories/',CategoriesView.as_view(),name='Categories'),
    path('subcategories/',SubCategoriesView.as_view(),name='SubCategories'),
    path('product/',ProductView.as_view(),name='Product'),
    path('products/',ProductsView.as_view(),name='Products'),
]