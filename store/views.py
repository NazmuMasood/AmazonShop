from store.models import Product
from django.shortcuts import render
from django.db.models import Q
from functools import reduce
import re

# Create your views here.
def store(request):
    products = Product.objects.all()
    context = {'products':products}
    
    # Getting the unique categories' list
    categoriesRaw = []
    for product in products:
        categoriesRaw.append(product.category)
    categories = list(dict.fromkeys(categoriesRaw))
    context['categories'] = categories

    context['currentPage'] = 'store'

    context['sorting_by'] = 'Default'
    sort_criterias = ['Default', 'Name (A - Z)', 'Name (Z - A)', 
                    'Price (Low > High)', 'Price (Low > High)' ]
    context['sort_criterias'] = sort_criterias

    return render(request, 'store/store.html', context)


def categoryByKey(request, key):
    products = Product.objects.filter(category=key).all()
    context = {'products':products}

    context['currentPage'] = 'categories'

    # Getting the unique categories' list
    allProducts = Product.objects.all()
    categoriesRaw = []
    for product in allProducts:
        categoriesRaw.append(product.category)
    categories = list(dict.fromkeys(categoriesRaw))
    context['categories'] = categories

    return render(request, 'store/store.html', context)


def search(request):
    # search_key = request.POST.get("search_key", "null")
    search_key = request.GET['search_key']
    print('search key: '+str(search_key))

    search_keys = re.split(r"[^A-Za-z']+", search_key)
    
    # search_fields = ('name', 'category', 'sub_category')
    # + "__icontains" <-- this produces a sql 'like' condition
    # q_objs = [Q(**{'%s' % i  + "__icontains": search_key}) for i in search_fields]
    # queries = reduce(lambda x, y: x | y, q_objs)

    q_objs = []
    search_fields = ('name', 'category', 'sub_category')
    for each_search_key in search_keys:
        # + "__icontains" <-- this produces a sql 'like' condition
        q_objs.extend([Q(**{'%s' % i  + "__icontains": each_search_key}) for i in search_fields])
    queries = reduce(lambda x, y: x | y, q_objs)

    products = Product.objects.filter(queries)
    context = {'products':products}
    context['search_key'] = search_key

    # Getting the unique categories' list
    allProducts = Product.objects.all()
    categoriesRaw = []
    for product in allProducts:
        categoriesRaw.append(product.category)
    categories = list(dict.fromkeys(categoriesRaw))
    context['categories'] = categories

    return render(request, 'store/store.html', context)