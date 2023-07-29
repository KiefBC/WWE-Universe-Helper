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


# TODO: Add Title Belt Option to Wrestler Entry
class IndexWrestlers(View):
    template_name = 'wrestler_index.html'

    # Select our SHOW_CHOICES
    show_choices = Shows.show_choices()

    def get(self, request):
        # Grab all of our Wrestlers
        wrestlers = Wrestlers.objects.all().order_by('name', 'weight_class')
        # Grab all of our Wrestlers Stats
        wrestler_stats = WrestlerStats.objects.all().order_by('wrestler__name', 'wrestler__weight_class')
        # Zip our Wrestlers and Wrestler Stats together
        wrestlers = zip(wrestlers, wrestler_stats)
        # Create our context
        context = {
            'wrestlers': wrestlers,
            'add_wrestler_form': AddWrestlerForm(),
            'weight_classes': WEIGHT_CLASSES,
            'show_choices': self.show_choices,
        }
        return render(request, self.template_name, context)

    def post(self, request):
        # Grab our Form
        form = AddWrestlerForm(request.POST)
        # Check if the form is valid
        if form.is_valid():
            # Save the form
            form.save()
            # Alert the user
            messages.success(request, f'{form.cleaned_data["name"]} has been added to the database')
            # Redirect to the coming_soon page
            return redirect('list_wrestlers')
        else:
            # Alert the user
            messages.error(request, f'Error: {form.errors}')
            # Redirect to the coming_soon page
            return redirect('list_wrestlers')


# TODO: All Show Titles should be Title Cased
# TODO: If Show Title is less than 3 characters, it should be capitalized
class IndexShows(View):
    template_name = 'show_index.html'

    def get(self, request):
        # Grab all of our Shows
        shows = set(Shows.objects.all().order_by('show_date'))
        # Grab our Form
        form = AddAShow()
        # Create our context
        context = {
            'shows': shows,
            'addShowForm': form,
            'choices': DAYS_OF_WEEK,
        }
        return render(request, self.template_name, context)

    def post(self, request):
        # Grab our Form
        form = AddAShow(request.POST)
        # Check if the form is valid
        if form.is_valid():

            # Clean up Show Name
            show_name = form.cleaned_data['show_name']
            # Check if any of the words in the show_name are less than 4 characters
            # If they are, capitalize them, else title case them
            show_name_split = show_name.split()
            show_name = ' '.join([word.upper() if len(word) <= 4 else word.title() for word in show_name_split])

            # Grab the show_date from the form
            show_date = form.cleaned_data['show_date']
            # Check if the show_date is occupied
            show_date_occupied = Shows.objects.filter(show_date=show_date).exists()

            if show_date_occupied:
                show_name_occupied = Shows.objects.get(show_date=show_date).show_name
                messages.error(request, f'{show_date} is already occupied by {show_name_occupied}')

                return redirect('list_shows')
            else:
                # Pass in our cleaned up show_name
                cleaned_up_form = AddAShow({'show_name': show_name, 'show_date': show_date})
                # Save the form
                cleaned_up_form.save()
                messages.success(request, 'Show added successfully')

                return redirect('list_shows')
        else:
            messages.error(request, 'Error: Invalid Form')
            return redirect('list_shows')
