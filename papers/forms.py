from django import forms


class SearchForm(forms.Form):
    q = forms.CharField(
        label="",
        max_length=300,
        required=True,
        widget=forms.TextInput(
            attrs={
                "placeholder": (
                    'Search papers... try "neural networks", '
                    "ai AND ethics, or transform*"
                ),
                "autofocus": True,
                "class": "search-input",
            }
        ),
    )