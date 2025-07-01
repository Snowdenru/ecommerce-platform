from django.urls import path
from .views import ProductCreateUpdateView, ProductListView, ProductDetailView


urlpatterns = [
    path("", ProductListView.as_view(), name="product-list"),
    path("<int:pk>/", ProductDetailView.as_view(), name="product-detail"),
    path("manage/", ProductCreateUpdateView.as_view(), name="product-manage"),
    path("manage/<int:pk>/", ProductCreateUpdateView.as_view(), name="product-manage-detail"),
]
