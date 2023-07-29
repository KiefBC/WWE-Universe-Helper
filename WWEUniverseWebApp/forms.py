from django import forms

from .models import Wrestlers, TitleBelts, Shows


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
        fields = ['name', 'weight_class', 'current_holder']

    def __init__(self, *args, **kwargs):
        super(AddTitleBelt, self).__init__(*args, **kwargs)
        # Inserting a unselectable option at the top of the Current Holder Select Field
        self.fields['current_holder'].queryset = Wrestlers.objects.all()
        self.fields['current_holder'].empty_label = 'Select Current Holder'
        # Allow Current Holder to be blank
        self.fields['current_holder'].required = False

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
        'current_holder': forms.Select(attrs={'class': 'form-control'}),
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
