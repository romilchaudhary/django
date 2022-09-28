from django.urls import path
# from .views import posts, login
from .views import enrollment, user_wise_courses, load_products, products, product_details
from .middleware import auth_middleware


urlpatterns = [
    # path('', auth_middleware(posts)),
    path('enrollment', auth_middleware(enrollment), name="enrollment"),
    path('enrolled/<int:pk>', user_wise_courses, name="enrolled" ),
    path('load-products/', load_products ),
    path('products/', products),
    path('product/<int:product_id>', product_details , name="product")
    # path('api/login', login)
    
]