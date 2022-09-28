# from django.conf import settings
# from django.db import models
# from django.contrib.auth.models import User, AbstractUser
# from django.db.models.signals import post_save, pre_delete, post_delete
# from django.dispatch import receiver
# import datetime
# from django.db.models import Count, Avg
# import datetime
# # from django.contrib.auth import get_user_model as user_model

# # User = user_model()


# # Create your models here.

# class CustomUser(models.Model):
#     user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
#     mobile = models.CharField(max_length=200, null=True, blank=True)
#     image = models.ImageField(upload_to="profile/pics", default="abc.png")
#     updated = models.DateField(default=datetime.datetime.now)

#     def __str__(self):
#         return str(self.user)

# class PostManager(models.Manager):
#     # def get_queryset(self, username):
#     #     return super().get_queryset().filter(author__username=username)
#     def small_than_comments(self, size):
#         return self.filter(comment__lte=size)

#     def greater_than_comments(self, size):
#         return self.filter(comment__gte=size)
    

# class Post(models.Model):
#     title = models.CharField(max_length=32)
#     author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="post_author")
#     created = models.DateField()
#     updated = models.DateField()
#     comment = models.IntegerField(default=0)
#     objects = PostManager()

#     def __str__(self):
#         return self.title

# class CommentPost(models.Model):
#     subject = models.CharField(max_length=200)
#     created = models.DateField()
#     comment_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comment_author")
#     post = models.ManyToManyField(Post, related_name="posts")

#     def __str__(self):
#         return self.subject

#     def get_posts(self):
#         return "\n".join([str(p) for p in self.post.all()])


# @receiver(post_save, sender=Post)
# def after_post_save(sender, instance, **kwargs):
#     print(f"post save instance is: {instance}")
#     print("after post save called")


# @receiver(post_save, sender=CommentPost)
# def post_save_commnet_save(sender, instance, **kwargs):
#     print("inside comment post save")
#     posts = list(CommentPost.objects.values_list('post', flat=True).distinct())
#     print(posts)
#     Post.objects.filter(pk__in=posts).update(updated=datetime.date.today())


# class Country(models.Model):
#     name = models.CharField(max_length=200, verbose_name="Country's First Name and Last Name")
#     city_count = models.IntegerField(default=0)

#     def __str__(self):
#         return self.name

#     class Meta:
#         verbose_name = "Country"
#         verbose_name_plural = "Countries"


# class City(models.Model):
#     name = models.CharField(max_length=200, verbose_name = "City's First And Last Name")
#     population = models.IntegerField(default=0)
#     country = models.ForeignKey(Country, on_delete=models.CASCADE)

#     def __str__(self):
#         return self.name

#     class Meta:
#         verbose_name = "City"
#         verbose_name_plural = "Cities"


# @receiver(post_save, sender=City)
# def city_post_save_reciever(sender, instance, **kwargs):
#     print(instance.country.id)
#     all_country_wise_cities_count = Country.objects.aggregate(city_count=Count('city'))
#     all_countries_with_city_count = Country.objects.filter(pk=instance.country.id).annotate(city_count_annotate=Count('city'))

#     print(all_country_wise_cities_count)
#     print(f"annotate : {vars(all_countries_with_city_count)}")

#     country = Country.objects.get(pk=instance.country.id)
#     country.city_count = all_countries_with_city_count[0].city_count_annotate
#     country.save()

#     avg_pop_total = Country.objects.aggregate(avg_popu=Avg('city__population'))
#     print(avg_pop_total)

#     avg_pop_country_wise = Country.objects.annotate(avg_pop = Avg('city__population'))
#     print(avg_pop_country_wise.query)
#     for data in avg_pop_country_wise:
#         print(data.avg_pop)


# @receiver(post_delete, sender=City)
# def city_post_delete(sender, instance, **kwargs):
#     country_id = instance.country.id
#     city_count_after_delete = Country.objects.filter(pk=country_id).aggregate(city_count = Count('city'))

#     country = Country.objects.get(pk=country_id)
#     country.city_count = city_count_after_delete["city_count"]
#     country.save()
    
# @receiver(post_save, sender=User)
# def post_save_user(sender, instance, created, **kwargs):
#     if created:
#         CustomUser.objects.create(user=instance, mobile=11111)
#     user_id = instance.id
#     profile = CustomUser.objects.get(user=user_id)
#     profile.updated = datetime.datetime.today()
#     profile.save()