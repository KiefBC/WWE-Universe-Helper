from django.contrib import messages
from django.core.management import call_command
from django.shortcuts import render, redirect
from django.views import View

from .forms import AddWrestlerForm, AddTitleBelt, AddAShow
from .models import WEIGHT_CLASSES, DAYS_OF_WEEK, Shows, TitleBelts, Wrestlers, WrestlerStats


class ComingSoon(View):
    template_name = 'coming_soon.html'

    # Select our Weight Classes and days of the week
    weight_classes = WEIGHT_CLASSES
    days_of_week = DAYS_OF_WEEK

    # Grab all of our Shows for our Show Select Field
    shows = Shows.objects.all().order_by('show_name')

    # Context for our template
    context = {
        'weight_classes': weight_classes,
        'days_of_week': days_of_week,
        'add_wrestler_form': AddWrestlerForm(),
        'add_title_form': AddTitleBelt(),
        'add_show_form': AddAShow(),
        'shows': shows,
    }

    def get(self, request):
        return render(request, self.template_name, self.context)

    def run_db_reset(request):
        """
        This method resets our database.
        :param request:
        :return:
        """

        try:
            # Call the db_reset command
            call_command('reset_db')
            # Redirect to the coming_soon page
            return redirect('coming_soon')
        except Exception as e:
            messages.error(request, f'Error: {e}')
            return redirect('coming_soon')

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

                form.save()

                return redirect('coming_soon')


class IndexWrestlers(View):
    template_name = 'wrestler_index.html'

    def get(self, request):
        # Grab all of our Wrestlers
        wrestlers = Wrestlers.objects.all().order_by('name', 'weight_class')
        # Grab all of our Wrestlers Stats
        wrestler_stats = WrestlerStats.objects.all().order_by('wrestler__name', 'wrestler__weight_class')
        # Grab all our Title Belts
        title_belts = TitleBelts.objects.all().order_by('name', 'weight_class')
        # Zip our Wrestlers and Wrestler Stats together
        wrestlers = zip(wrestlers, wrestler_stats)
        # Create our context
        context = {
            'wrestlers': wrestlers,
        }
        return render(request, self.template_name, context)
