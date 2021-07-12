from django.urls import path

from . import views

urlpatterns = [
	path('', views.store, name="store"),
	# path('/', views.store, name="store"),

	path('category/<str:key>', views.categoryByKey, name='categoryByKey'),
	
	path('search', views.search, name='search'),


]
