from django import forms

from OnlineCookbook.common.models import Comment
from OnlineCookbook.recipes.models import Recipe


class CommentForm(forms.ModelForm):
    recipe_pk = forms.IntegerField(
        widget=forms.HiddenInput(),
    )
    text = forms.CharField(
        widget=forms.Textarea(),
    )

    class Meta:
        model = Comment
        fields = ('text', 'recipe_pk')

    def save(self, commit=True):
        recipe_pk = self.cleaned_data['recipe_pk']
        recipe = Recipe.objects.get(pk=recipe_pk)

        comment = Comment(
            recipe=recipe,
            text=self.cleaned_data['text'],
        )
        if commit:
            comment.save()

        return comment


class SearchForm(forms.Form):
    text = forms.CharField()
