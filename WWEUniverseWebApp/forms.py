from django import forms

from .models import Wrestlers, TitleBelts, Shows, WrestlerStats, TitleHolders
from .helpers import MONTHS, WEIGHT_CLASSES, DAYS_OF_WEEK


class AddWrestlerForm(forms.ModelForm):
    """
    This is our form for adding a Wrestler to our Wrestlers Table.
    """

    class Meta:
        model = Wrestlers
        fields = ['name', 'weight_class']

    widgets = {
        'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Wrestler Name'}),
        'weight_class': forms.Select(attrs={'class': 'form-control'})
    }


class AddTitleBelt(forms.ModelForm):
    """
    This is our form for adding a Title Belt to our Title Belts Table.
    """

    class Meta:
        model = TitleBelts
        fields = ['name', 'weight_class']

    def save(self, commit=True):
        """
        This method overrides the save method to capitalize the name before saving it to the database.
        :param commit:
        :return:
        """
        instance = super().save(commit=False)
        instance.name = instance.name.title()

        if commit:
            instance.save()

        return instance

    widgets = {
        'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title Belt Name'}),
        'weight_class': forms.Select(attrs={'class': 'form-control'}),
    }


class AddTitleBeltWrestler(forms.ModelForm):
    """
    This is our form for only adding existing Title Belts to Wrestlers.
    """

    class Meta:
        model = TitleHolders
        fields = ['wrestler', 'title_belt', 'month_won', 'day_won', 'year_won']

    widgets = {
        'wrestler': forms.Select(attrs={'class': 'form-control'}),
        'title_belt': forms.Select(attrs={'class': 'form-control'}),
        'month_won': forms.Select(attrs={'class': 'form-control'}),
        'day_won': forms.Select(attrs={'class': 'form-control'}),
        'year_won': forms.Select(attrs={'class': 'form-control'}),
    }


class AddAShow(forms.ModelForm):
    """
    This is our form for adding a Show to our Shows Table.
    """

    class Meta:
        model = Shows
        fields = ['show_name', 'show_date']

    # def save(self, commit=True):
    #     """
    #     This method overrides the save method to capitalize the show_name before saving it to the database.
    #     :param commit:
    #     :return:
    #     """
    #     instance = super().save(commit=False)
    #     instance.show_name = instance.show_name.lower()
    #
    #     if commit:
    #         instance.save()
    #
    #     return instance

    widgets = {
        'show_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Show Name'}),
        'show_date': forms.Select(attrs={'class': 'form-control'})
    }


class UpdateStats(forms.ModelForm):
    """
    This is our form for updating a Wrestler's Stats.
    """
    wrestler = forms.ModelChoiceField(
        queryset=Wrestlers.objects.all(),
        widget=forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
    )

    class Meta:
        model = WrestlerStats
        fields = ['wins', 'losses', 'wrestler']

    widgets = {
        'wins': forms.NumberInput(attrs={'class': 'form-control'}),
        'losses': forms.NumberInput(attrs={'class': 'form-control'}),
    }
