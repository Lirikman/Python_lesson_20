from datetime import datetime

from rest_framework import serializers
from .models import Article, Problem, Order


class ArticleSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    image = serializers.ImageField(default='main/info.jpg')

    class Meta:
        model = Article
        fields = ('id', 'name', 'text', 'image', 'user')


class ProblemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Problem
        fields = '__all__'


class OrdersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('id', 'client', 'phone', 'problem')


class ClientsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'
