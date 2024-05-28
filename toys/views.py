from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Toy
from .serializers import ToySerializer

class ToyViewSet(viewsets.ModelViewSet):
    queryset = Toy.objects.all()
    serializer_class = ToySerializer

    def update_by_name(self, request, name=None):
        try:
            toy = Toy.objects.get(name=name)
        except Toy.DoesNotExist:
            return Response({'error': 'Toy not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = self.get_serializer(toy, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete_by_name(self, request, name=None):
        try:
            toy = Toy.objects.get(name=name)
        except Toy.DoesNotExist:
            return Response({'error': 'Toy not found'}, status=status.HTTP_404_NOT_FOUND)

        toy.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)