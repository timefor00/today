from django import forms


class AddProductForm(forms.Form):

    is_update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)