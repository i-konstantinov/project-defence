from django import forms

from OnlineCookbook.recipes.models import Recipe


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        exclude = ('user',)
        widgets = {
            'ingredients': forms.Textarea(),
            'instructions': forms.Textarea(),
        }
