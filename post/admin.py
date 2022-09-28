from django.contrib import admin
from .models.enrollment import Student, Course, Enrollment
from .models.product import Product

admin.site.register(Student)
admin.site.register(Course)
admin.site.register(Enrollment)
admin.site.register(Product)
# from .models import Post, CommentPost, Country, City, CustomUser
# # Register your models here.

# @admin.register(Post)
# class PostAdmin(admin.ModelAdmin):
#     fields = ('title', 'author', 'created', 'updated', 'comment')
#     list_display = ('id', 'title', 'author', 'created', 'updated', 'comment')
#     empty_value_display = 'NA'


# @admin.register(CommentPost)
# class CommentPostAdmin(admin.ModelAdmin):
#     fields = ("subject", "created", "comment_user", "post")
#     list_display = ("id", "subject", "created", "comment_user", "get_posts")
#     empty_value_display = 'NA'

# @admin.register(Country)
# class CountryAdmin(admin.ModelAdmin):
#     fields = ("name", "city_count")
#     readonly_fields=('city_count', )
#     list_display = ("id", "name", "city_count")
#     empty_value_display = "NA"


# @admin.register(City)
# class CityAdmin(admin.ModelAdmin):
#     fields = ("name", "population" , "country")
#     list_display = ("id", "name", "population" , "country")
#     empty_value_display = "NA"

# admin.site.register(CustomUser)