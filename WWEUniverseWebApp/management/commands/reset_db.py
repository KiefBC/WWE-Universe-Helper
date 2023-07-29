import random
import time
from django.core.management import call_command, BaseCommand

import WWEUniverseWebApp.models


class Command(BaseCommand):
    help = 'Reset database and populate it with data'

    def handle(self, *args, **options):
        # Reset DB
        print('Flushing the Database')
        call_command('flush', interactive=False)
        print('Doing our initial migrations')
        call_command('makemigrations')
        # time.sleep(3)
        call_command('migrate')

        # Populate Our Wrestlers Table With Some Data
        print('Populating Wrestler Table')
        wrestlers = {
            'Roman Reigns': {'weight_class': 'HW'},
            'Jey USO': {'weight_class': 'HW'},
            'Jimmy USO': {'weight_class': 'HW'},
            'Drew McIntyre': {'weight_class': 'HW'},
            'Bobby Lashley': {'weight_class': 'HW'},
            'Sheamus': {'weight_class': 'LHW'},
            'Randy Orton': {'weight_class': 'HW'},
            'AJ Styles': {'weight_class': 'HW'},
            'Jeff Hardy': {'weight_class': 'HW'},
            'Kofi Kingston': {'weight_class': 'LHW'},
            'Xavier Woods': {'weight_class': 'CW'},
            'Big E': {'weight_class': 'CW'},
            'The Miz': {'weight_class': 'CW'},
            'John Morrison': {'weight_class': 'LHW'},
            'Riddle': {'weight_class': 'CW'},
            'Keith Lee': {'weight_class': 'CW'},
            'Braun Strowman': {'weight_class': 'LHW'},
            'Shelton Benjamin': {'weight_class': 'LHW'},
            'Cedric Alexander': {'weight_class': 'LHW'},
            'Elias': {'weight_class': 'HW'},
            # etc.
        }

        for name, attrs in wrestlers.items():
            wrestler, created = WWEUniverseWebApp.models.Wrestlers.objects.update_or_create(
                name=name,
                weight_class=attrs['weight_class'],
            )
            if created:
                wrestler.save()
                print(f'Added {name} to the Wrestlers Table')
            else:
                print(f'{name} already exists in the Wrestlers Table')

        # Populate Our Shows Table With Some Data
        print('Populating Shows Table')
        shows = {
            'RAW': {'show_date': 'MON'},
            'Smackdown': {'show_date': 'FRI'},
            'NXT': {'show_date': 'TUE'},
            'AEW': {'show_date': 'WED'},
        }

        for show, attrs in shows.items():
            show, created = WWEUniverseWebApp.models.Shows.objects.update_or_create(
                show_name=show,
                show_date=attrs['show_date'],
            )
            if created:
                show.save()
                print(f'Added {show} to the Shows Table')
            else:
                print(f'{show} already exists in the Shows Table')

        # Populate Our Title Belts Table With Some Data
        print('Populating Title Belts Table')
        title_belts = {
            'WWE Universal Championship': {'weight_class': 'HW'},
            'WWE Championship': {'weight_class': 'HW'},
            'WWE Intercontinental Championship': {'weight_class': 'LHW'},
            'WWE United States Championship': {'weight_class': 'CW'},
        }

        for title, attrs in title_belts.items():
            title_belt, created = WWEUniverseWebApp.models.TitleBelts.objects.update_or_create(
                name=title,
                weight_class=attrs['weight_class'],
            )
            if created:
                title_belt.save()
                print(f'Added {title} to the Title Belts Table')
            else:
                print(f'{title} already exists in the Title Belts Table')

        # Add a random win and loss to each wrestler
        print('Adding random wins and losses to each wrestler')
        wins_losses = {}
        # Loop through each wrestler and update the dictionary with values
        for wrestler in WWEUniverseWebApp.models.Wrestlers.objects.all():
            wins_losses[wrestler.name] = {'wins': random.randint(0, 100), 'losses': random.randint(0, 100)}
        # Apply the dictionary to the WrestlerStats Table
        for wrestler, attrs in wins_losses.items():
            WWEUniverseWebApp.models.WrestlerStats.objects.update_or_create(
                wrestler=WWEUniverseWebApp.models.Wrestlers.objects.get(name=wrestler),
                wins=attrs['wins'],
                losses=attrs['losses'],
            )
            print(f'Added {attrs["wins"]} wins and {attrs["losses"]} losses to {wrestler}')
