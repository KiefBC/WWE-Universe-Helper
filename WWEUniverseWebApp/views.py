from django.contrib import messages
from django.shortcuts import render, redirect
from django.views import View

from .forms import AddWrestlerForm, AddTitleBelt, AddAShow
from .models import WEIGHT_CLASSES, DAYS_OF_WEEK, Shows, TitleBelts

# TODO: Add Real Website
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
        # TODO: Add Logic
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

            # LOGIC
            # Can't have two shows on the same day
            # Can't have two shows with the same name
            # Can't have two shows with the same name on the same day
            # END LOGIC

            form = AddAShow(request.POST)
            if form.is_valid():

                # Grab the show_date from the form
                show_date = form.cleaned_data['show_date']
                # Check if the show_date is occupied
                show_date_occupied = Shows.objects.filter(show_date=show_date).exists()

                if show_date_occupied:
                    show_name_occupied = Shows.objects.get(show_date=show_date).show_name
                    messages.error(request, f'{show_date} is already occupied by {show_name_occupied}')

                    return redirect('coming_soon')
                else:
                    # Save the form
                    form.save()

                    return redirect('coming_soon')

        # TODO: Add Logic
        # Submitting new Title Belt
        elif 'add_title_form' in request.POST:
            form = AddTitleBelt(request.POST)
            if form.is_valid():
                # LOGIC
                # Can't have two title belts with the same name
                # Can't have two title belts with the same name on the same show
                # A Weight Class must be selected

                # Form Data
                title_name = form.cleaned_data['name'].title()

                # Check if the title_name is occupied
                title_name_occupied = TitleBelts.objects.filter(name=title_name).exists()
                if title_name_occupied:
                    messages.error(request, f'The name "{title_name}" is already occupied')
                    return redirect('coming_soon')

                # Check if the title_name is occupied on the same show
                show_name = form.cleaned_data['show']
                title_name_occupied_on_show = TitleBelts.objects.filter(name=title_name, show=show_name).exists()
                if title_name_occupied_on_show:
                    messages.error(request,
                                   f'"{title_name}" is unfortunately already occupied on <{show_name}>. Please pick another Show or pick another Title Name')
                    return redirect('coming_soon')


                form.save()
                return redirect('coming_soon')
