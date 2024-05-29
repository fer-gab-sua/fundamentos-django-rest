from rest_framework import serializers
from user.models import Producto , Article

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = '__all__' #todos los campos del modelo producto

class Producto2Serializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = ['nombre','descripcion', 'marca', 'cantidad_min','title', 'content', 'author', 'published_date']  #todos los campos del modelo producto



class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['title', 'content', 'author']   # Excluye 'published_date'


class ArticleAuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['author', 'title'] # Solo incluye el campo 'author'

class ArticleSerializerFull(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['title', 'content', 'author', 'published_date']  