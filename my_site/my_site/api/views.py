from rest_framework import viewsets , status
from rest_framework.response import Response
from user.models import Producto , Article
from my_site.api.serializer import ProductoSerializer , ArticleSerializer , ArticleAuthorSerializer, ArticleSerializerFull



class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

    def create(self,request,*args,**kwargs):
        data_copy = request.data.copy()#hago una copia del data del request
        print(data_copy)
        data_copy['published_date'] = '2024-05-28' #agrego el campo que quiero
        serializer = ArticleSerializerFull(data=data_copy) #lo mando al serializador que esta con la tabla completa el "full"
        if serializer.is_valid(): #valido los datos
            serializer.save() #lo salvo
            # Devolver una respuesta de éxito con el objeto creado y un código 201 (CREATED)
            instance = serializer.save()
            # Imprimo el ID asignado al objeto por consola
            print("ID asignado al objeto:", instance.id)
            
            producto_data = {'nombre' : instance.id,
                            'descripcion' : "hola",
                            'marca' : "como estas",
                            'cantidad_min' : 1,
                            'cantidad_max' : 10,
                            'precio' : 1.5
                            }  # Asignamos el ID del artículo al campo article_id
            producto_serializer = ProductoSerializer(data=producto_data)
            if producto_serializer.is_valid():
                producto_serializer.save()

            response_data = {
                'id': instance.id,
                **serializer.data  # Incluimos los datos del artículo
            }

            return Response(response_data, status=status.HTTP_201_CREATED) #retorno el data completo
        # Si los datos no son válidos, devolver una respuesta de error con los errores de validación
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def list(self,request,*args,**kwargs):
        queryset = self.get_queryset()
        serializer = ArticleAuthorSerializer(queryset, many=True)
        return Response(serializer.data)
    