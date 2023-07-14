from rest_framework import status
from rest_framework.response import Response


class GetObjectMixin:
    """ Миксин для добавления/удаления рецептов в избранное/корзину. """

    def post_recipe(self, model_class, model_serializer):
        data = {
            'user': request.user.id,
            'recipe': id
        }
        if not model_class.objects.filter(
           user=request.user, recipe__id=id).exists():
            serializer = model_serializer(
                data=data, context={'request': request}
            )
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(
                serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    def del_recipe(self, model_class, recipe):
        if model_class.objects.filter(
           user=request.user, recipe=recipe).exists():
            model_class.objects.filter(user=request.user, recipe=recipe).delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_400_BAD_REQUEST)
