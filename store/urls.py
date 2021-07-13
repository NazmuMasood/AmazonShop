from django.urls import path

from . import views

urlpatterns = [
	path('', views.store, name="store"),
	path('sort-by/<str:sort_key>', views.storeSort, name="storeSort"),
 
	path('category/<str:key>', views.categoryByKey, name='categoryByKey'),
	path('category/<str:key>/sort-by/<str:sort_key>', views.categoryByKeySort, name="categorySort"),

	path('search', views.search, name='search'), 
	path('search/<str:key>/sort-by/<str:sort_key>', views.searchSort, name="searchSort"),
  
]
