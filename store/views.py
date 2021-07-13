from store.models import Product
from django.shortcuts import render
from django.db.models import Q
from functools import reduce
import re

#------ /store endpoints
def store(request):
    products = Product.objects.all()
    context = {'products':products}
     
    # Getting the unique categories' list
    categoriesDict = Product.objects.order_by("category").values('category').distinct()
    categories = []
    for product in categoriesDict:
        categories.append(product['category'])
    context['categories'] = categories

    context['currentPage'] = 'store'

    context['sorting_by'] = 'Default'
    sort_criterias = ['Default', 'Name (A - Z)', 'Name (Z - A)', 
                    'Price (Low > High)', 'Price (High > Low)' ]
    context['sort_criterias'] = sort_criterias

    return render(request, 'store/store.html', context)


def storeSort(request, sort_key):
    if sort_key == 'Default':
        products = Product.objects.all()
    elif sort_key == 'Name (A - Z)':
        products = Product.objects.order_by('name').all()
    elif sort_key == 'Name (Z - A)':
        products = Product.objects.order_by('-name').all()
    elif sort_key == 'Price (Low > High)':
        products = Product.objects.order_by('price').all()
    elif sort_key == 'Price (High > Low)':
        products = Product.objects.order_by('-price').all()

    context = {'products':products}

    # Getting the unique categories' list
    categoriesDict = Product.objects.order_by("category").values('category').distinct()
    categories = []
    for product in categoriesDict:
        categories.append(product['category'])
    context['categories'] = categories

    context['currentPage'] = 'store'

    context['sorting_by'] = sort_key
    sort_criterias = ['Default', 'Name (A - Z)', 'Name (Z - A)', 
                    'Price (Low > High)', 'Price (High > Low)' ]
    context['sort_criterias'] = sort_criterias

    return render(request, 'store/store.html', context)


#------ /category endpoints
def categoryByKey(request, key):
    products = Product.objects.filter(category=key).all()
    context = {'products':products}

    context['currentPage'] = 'categories'

   # Getting the unique categories' list
    categoriesDict = Product.objects.order_by("category").values('category').distinct()
    categories = []
    for product in categoriesDict:
        categories.append(product['category'])
    context['categories'] = categories
    context['currentCategory'] = key

    context['sorting_by'] = 'Default'
    sort_criterias = ['Default', 'Name (A - Z)', 'Name (Z - A)', 
                    'Price (Low > High)', 'Price (High > Low)' ]
    context['sort_criterias'] = sort_criterias

    return render(request, 'store/store.html', context)

def categoryByKeySort(request, key, sort_key):
    if sort_key == 'Default':
        products = Product.objects.filter(category=key).all()
    elif sort_key == 'Name (A - Z)':
        products = Product.objects.filter(category=key).order_by('name').all()
    elif sort_key == 'Name (Z - A)':
        products = Product.objects.filter(category=key).order_by('-name').all()
    elif sort_key == 'Price (Low > High)':
        products = Product.objects.filter(category=key).order_by('price').all()
    elif sort_key == 'Price (High > Low)':
        products = Product.objects.filter(category=key).order_by('-price').all()
    context = {'products':products}

    context['currentPage'] = 'categories'

    # Getting the unique categories' list
    categoriesDict = Product.objects.order_by("category").values('category').distinct()
    categories = []
    for product in categoriesDict:
        categories.append(product['category'])
    context['categories'] = categories
    context['currentCategory'] = key

    context['sorting_by'] = sort_key
    sort_criterias = ['Default', 'Name (A - Z)', 'Name (Z - A)', 
                    'Price (Low > High)', 'Price (High > Low)' ]
    context['sort_criterias'] = sort_criterias

    return render(request, 'store/store.html', context)


#------- /search endpoints
def search(request):
    # search_key = request.POST.get("search_key", "null")
    search_key = request.GET['search_key'].strip()
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
    context['currentPage'] = 'search'

    # Getting the unique categories' list
    categoriesDict = Product.objects.order_by("category").values('category').distinct()
    categories = []
    for product in categoriesDict:
        categories.append(product['category'])
    context['categories'] = categories

    # 'sorting dropdown menu' values
    context['sorting_by'] = 'Default'
    sort_criterias = ['Default', 'Name (A - Z)', 'Name (Z - A)', 
                    'Price (Low > High)', 'Price (High > Low)' ]
    context['sort_criterias'] = sort_criterias

    return render(request, 'store/store.html', context)


def searchSort(request, key, sort_key):
    search_key = key.strip()
    print('search key: '+str(search_key))

    search_keys = re.split(r"[^A-Za-z']+", search_key)

    q_objs = []
    search_fields = ('name', 'category', 'sub_category')
    for each_search_key in search_keys:
        # + "__icontains" <-- this produces a sql 'like' condition
        q_objs.extend([Q(**{'%s' % i  + "__icontains": each_search_key}) for i in search_fields])
    queries = reduce(lambda x, y: x | y, q_objs)

    if sort_key == 'Default':
        products = Product.objects.filter(queries).all()
    elif sort_key == 'Name (A - Z)':
        products = Product.objects.filter(queries).order_by('name').all()
    elif sort_key == 'Name (Z - A)':
        products = Product.objects.filter(queries).order_by('-name').all()
    elif sort_key == 'Price (Low > High)':
        products = Product.objects.filter(queries).order_by('price').all()
    elif sort_key == 'Price (High > Low)':
        products = Product.objects.filter(queries).order_by('-price').all()
    context = {'products':products}
    context['search_key'] = search_key
    context['currentPage'] = 'search'

    # Getting the unique categories' list
    categoriesDict = Product.objects.order_by("category").values('category').distinct()
    categories = []
    for product in categoriesDict:
        categories.append(product['category'])
    context['categories'] = categories

    # 'sorting dropdown menu' values
    context['sorting_by'] = sort_key
    sort_criterias = ['Default', 'Name (A - Z)', 'Name (Z - A)', 
                    'Price (Low > High)', 'Price (High > Low)' ]
    context['sort_criterias'] = sort_criterias

    return render(request, 'store/store.html', context)

 