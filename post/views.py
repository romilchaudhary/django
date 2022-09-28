from django.shortcuts import render
# from .models import Post
from .models.enrollment import Student, Course, Enrollment
from .models.product import Product

from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)
from rest_framework.response import Response

from itertools import chain
import requests

# Create your views here.

# def posts(request):
#     all_posts = Post.objects.order_by("-created")
#     comment_counts= 2
#     small_comments_count_posts = Post.objects.small_than_comments(comment_counts)
#     gretaer_than_comments= Post.objects.greater_than_comments(comment_counts)
#     context = {
#         'all_posts': all_posts,
#         'small_comments': small_comments_count_posts,
#         'greater_comments': gretaer_than_comments
#     }
#     return render(request, 'posts/posts.html', context) 

# @csrf_exempt
# @api_view(["POST"])
# @permission_classes((AllowAny,))
# def login(request):
#     username = request.data.get("username")
#     password = request.data.get("password")
#     if username is None or password is None:
#         return Response({'error': 'Please provide both username and password'},
#                         status=HTTP_400_BAD_REQUEST)
#     user = authenticate(username=username, password=password)
#     if not user:
#         return Response({'error': 'Invalid Credentials'},
#                         status=HTTP_404_NOT_FOUND)
#     token, _ = Token.objects.get_or_create(user=user)
#     print(token, _)
#     return Response({'token': token.key},
#                     status=HTTP_200_OK)



def enrollment(request):
    queryset = Student.objects.all()
    context = {
        'results': queryset
    }
    return render(request, 'posts/enrollment.html', context)

def user_wise_courses(request, pk):
    user_obj = Student.objects.get(pk=pk)
    # queryset = user_obj.course_set.all()
    enrolled = Enrollment.objects.filter(student=user_obj)
    print(enrolled)

    context = {
        # 'results': list(chain(queryset, enrolled))
        'results': enrolled
    }

    return render(request, 'posts/enrolled.html', context)

def products(request):
    products = Product.objects.all()
    context = {
        'results': products
    }
    return render(request, 'posts/index.html', context)


def product_details(request, product_id):
    product = Product.objects.get(pk=product_id)
    recently_viewed_products = None

    if 'recently_viewed' in request.session:
        if product_id in request.session['recently_viewed']:
            request.session['recently_viewed'].remove(product_id)
        
        products = Product.objects.filter(pk__in=request.session['recently_viewed'])
        recently_viewed_products = sorted(products, key=lambda x: request.session['recently_viewed'].index(x.id))
        request.session['recently_viewed'].insert(0, product_id)
    else:
        request.session['recently_viewed'] = [product_id]

    request.session.modified = True
    context = {
        'product': product,
        'recently_viewed': recently_viewed_products[:5]
    } 
    return render(request, 'posts/product-details.html', context)

def load_products(request):
    r = requests.get("https://fakestoreapi.com/products")
    products = r.json()
    for product in products:
        results = Product(
            title= product['title'],
            description= product['description'],
            price= product['price'],
            image_url= product['image']
        )
        results.save()
    context = {
        'results': products
    }
    return render(request, 'posts/index.html', context)