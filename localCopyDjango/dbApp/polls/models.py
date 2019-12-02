import datetime
from django.db import models as sqlModels
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator
from djongo import models as noSQLModels

# Create your models here.
class User(sqlModels.Model):
    def __str__(self):
        return self.user_name
    user_name = sqlModels.CharField(max_length=50, unique=True)
    date_created = sqlModels.DateTimeField('date created')
    location = sqlModels.CharField(max_length=50)
    favorite_restaurant = sqlModels.CharField(max_length=50)

class Restaurant(sqlModels.Model):
    def __str__(self):
        return self.restaurant_name
    restaurant_name = sqlModels.CharField(max_length=50)
    location = sqlModels.CharField(max_length=50)
    # only one primary key in sqlite
    price_tier = sqlModels.CharField(max_length=4)
    rating = sqlModels.DecimalField(max_digits=2, decimal_places = 1)
    # hours is a separate table
    # cuisine tags, reviews is NoSQL

class Menu(sqlModels.Model):
    def __str__(self):
        return self.restaurant_name
    restuarant_name = sqlModels.ForeignKey('Restaurant', on_delete=sqlModels.CASCADE)
    food_type = sqlModels.CharField(max_length=20)
    dietary_restrictions = sqlModels.CharField(max_length=50)
    price = sqlModels.IntegerField(default=0,
        validators=[MaxValueValidator(1), MinValueValidator(10)])

class Hours(sqlModels.Model):
    def __str__(self):
        return self.restaurant_name
    restaurant_name = sqlModels.ForeignKey('Restaurant', on_delete=sqlModels.CASCADE)
    m_open = sqlModels.CharField(max_length=8)
    m_close = sqlModels.CharField(max_length=8)
    t_open = sqlModels.CharField(max_length=8)
    t_close = sqlModels.CharField(max_length=8)
    w_open = sqlModels.CharField(max_length=8)
    w_close = sqlModels.CharField(max_length=8)
    th_open = sqlModels.CharField(max_length=8)
    th_close = sqlModels.CharField(max_length=8)
    f_open = sqlModels.CharField(max_length=8)
    f_close = sqlModels.CharField(max_length=8)
    sa_open = sqlModels.CharField(max_length=8)
    sa_close = sqlModels.CharField(max_length=8)
    su_open = sqlModels.CharField(max_length=8)
    su_close = sqlModels.CharField(max_length=8)

class Reviews(noSQLModels.Model):
    def __str__(self):
        return self.review_title
    review_title = noSQLModels.CharField(max_length=30)
    restaurant_name = noSQLModels.CharField(max_length=50)
    user_name = noSQLModels.CharField(max_length=50, unique=True)
    date_written = noSQLModels.DateTimeField('date written')
    review_text = noSQLModels.CharField(max_length=250)
    star_rating = noSQLModels.DecimalField(max_digits=2, decimal_places=1)
