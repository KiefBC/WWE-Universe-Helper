from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from .models import WEIGHT_CLASSES, DAYS_OF_WEEK, Wrestlers, Shows
from .forms import AddWrestlerForm, AddTitleBelt, AddAShow


# Create your views here.
class ComingSoon(View):
    template_name = 'coming_soon.html'

    # Select our Weight Classes and days of the week
    weight_classes = WEIGHT_CLASSES
    days_of_week = DAYS_OF_WEEK

    # Context for our template
    context = {
        'weight_classes': weight_classes,
        'days_of_week': days_of_week,
        'add_wrestler_form': AddWrestlerForm(),
        'add_title_form': AddTitleBelt(),
        'add_show_form': AddAShow(),
    }

    def get(self, request):
        return render(request, self.template_name, self.context)

    def post(self, request):
        """
        This method adds a Wrestler to our Wrestlers Table.
        :param request:
        :return:
        """
        # Submitting new Wrestler
        if 'add_wrestler_form' in request.POST:
            # Create an instance of our AddWrestlerForm
            form = AddWrestlerForm(request.POST)
            # Check if the form is valid
            if form.is_valid():
                # Save the form
                form.save()
                # Redirect to the coming_soon page
                return redirect('coming_soon')

        # Submitting new Show
        elif 'add_show_form' in request.POST:
            form = AddAShow(request.POST)
            if form.is_valid():

                # Grab the show_date from the form
                show_date = form.cleaned_data['show_date']

                # Check if the show_date is occupied
                show_date_occupied = Shows.objects.filter(show_date=show_date).exists()

                if show_date_occupied:

                    # Grab the show_name of the show that is already occupying the show_date
                    show_name_occupied = Shows.objects.get(show_date=show_date).show_name
                    messages.error(request, f'{show_date} is already occupied by {show_name_occupied}')

                    return redirect('coming_soon')
                else:

                    form.save()

                    return redirect('coming_soon')

        # Submitting new Title Belt
        elif 'add_title_form' in request.POST:
            form = AddTitleBelt(request.POST)
            if form.is_valid():
                form.save()
                return redirect('coming_soon')
