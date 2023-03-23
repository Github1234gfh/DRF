from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class Allview(APIView):
    model = None
    serializer_class = None
    
    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        try:
            if not pk:
                objects = self.model.objects.all()
                serializer = self.serializer_class(objects, many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)
            object = self.model.objects.get(pk=pk)
            serializer = self.serializer_class(object)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            return Response({'not found'}, status=status.HTTP_404_NOT_FOUND)
    
    def post(self, request):
        seriolizer = self.serializer_class(data=request.data, context={'request': request})
        if seriolizer.is_valid(raise_exception=True):
                seriolizer.save()
                return Response(seriolizer.data, status=status.HTTP_201_CREATED)
        return Response(seriolizer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)

        try:
            isinstance = self.model.objects.get(pk=pk)
        except:
            return Response({'error': 'object is not exist'}, status=status.HTTP_404_NOT_FOUND)
        
        seriolizer = self.serializer_class(data=request.data,context={'request': request} , instance=isinstance)
        if seriolizer.is_valid(raise_exception=True):
            seriolizer.save()
            return Response({'post': seriolizer.data}, status=status.HTTP_201_CREATED)
        return Response(seriolizer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)

        try:
            object = self.model.objects.get(pk=pk)
        except:
            return Response({'error':"object doesnt exist"}, status=status.HTTP_404_NOT_FOUND)
        
        object.delete()
        return Response({"object": f"delete {str(pk)}"}, status=status.HTTP_204_NO_CONTENT)

