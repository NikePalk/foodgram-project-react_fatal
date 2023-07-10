class GetObjectMixin:
    """ Миксин для добавления/удаления рецептов в избранное/корзину. """

    def check_if_exists(self, model_class, recipe):
        return model_class.objects.filter(
            user=self.request.user, recipe=recipe).exists(
        )

    def del_recipe(self, model_class, recipe):
        return model_class.objects.filter(
            user=self.request.user, recipe=recipe).delete(
        )