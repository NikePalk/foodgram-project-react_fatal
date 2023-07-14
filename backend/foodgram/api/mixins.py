from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response

from recipes.models import Recipe


class GetObjectMixin:
    """ Миксин для добавления/удаления рецептов в избранное/корзину. """

    def post_recipe(self, request, id):
        data = {
            'user': request.user.id,
            'recipe': id
        }
        if not self.model_class.objects.filter(
           user=request.user, recipe__id=id).exists():
            serializer = self.model_serializer(
                data=data, context={'request': request}
            )
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(
                serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    def del_recipe(self, request, id):
        recipe = get_object_or_404(Recipe, id=id)
        if self.model_class.objects.filter(
           user=request.user, recipe=recipe).exists():
            self.model_class.objects.filter(
                user=request.user,
                recipe=recipe
            ).delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_400_BAD_REQUEST)
